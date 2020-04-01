# -*- coding: utf-8 -*-
from .. import BrukerLoader, __version__
import argparse
import os, re


def main():
    parser = argparse.ArgumentParser(prog='brkraw.py',
                                     description="Command line tool of Bruker Rawdata Handler")
    parser.add_argument("-v", "--version", action='version', version='%(prog)s v{}'.format(__version__))

    subparsers = parser.add_subparsers(title='Sub-commands',
                                       description='brkraw.py provides two major function reporting '
                                                   'contents on bruker raw data '
                                                   'and converting image data into NifTi format.',
                                       help='description',
                                       dest='function',
                                       metavar='command')

    summary = subparsers.add_parser("summary", help='Print out data summary')
    summary.add_argument("path", help="Folder location for the Bruker raw data", type=str)

    gui = subparsers.add_parser("gui", help='Start GUI')
    gui.add_argument("-i", "--input", help="Folder location for the Bruker raw data", type=str, default=None)
    gui.add_argument("-o", "--output", help="Folder location for converted NifTi data", type=str, default=None)

    nii = subparsers.add_parser("tonii", help='Convert to NifTi format')
    nii.add_argument("path", help="Folder location for the Bruker raw data", type=str)
    nii.add_argument("-b", "--bids", help="Create JSON file with BIDS standard MRI acqusition parameter.", action='store_true')
    nii.add_argument("-o", "--output", help="Filename w/o extension to export NifTi image", type=str, default=False)
    nii.add_argument("-r", "--recoid", help="RECO ID (if scan_id has multiple reconstruction data)", type=int, default=1)
    nii.add_argument("-s", "--scanid", help="Scan ID", type=str)

    niiall = subparsers.add_parser("tonii_all", help="Convert All Datasets inside input path, "
                                                     "Caution: Don't use this function on console computer!! "
                                                     "It will take forever!!")
    niiall.add_argument("path", help="Path of dataset root folder", type=str)
    niiall.add_argument("-b", "--bids", help="Create JSON file with BIDS standard MRI acqusition parameter.",
                        action='store_true')

    args = parser.parse_args()

    if args.function == 'summary':
        path = args.path
        if any([os.path.isdir(path), ('zip' in path), ('PvDataset' in path)]):
            study = BrukerLoader(path)
            study.summary()
        else:
            list_path = [d for d in os.listdir('.') if (any([os.path.isdir(d),
                                                             ('zip' in d),
                                                             ('PvDataset' in d)]) and re.search(path, d, re.IGNORECASE))]
            for p in list_path:
                study = BrukerLoader(p)
                study.summary()

    elif args.function == 'gui':
        ipath = args.input
        opath = args.output
        from ..ui.main_win import MainWindow
        root = MainWindow()
        if ipath != None:
            root._path = ipath
            root._extend_layout()
            root._load_dataset()
        if opath != None:
            root._output = opath
        root.mainloop()

    elif args.function == 'tonii':
        path = args.path
        scan_id = args.scanid
        reco_id = args.recoid
        study = BrukerLoader(path)
        if args.output:
            output = args.output
        else:
            output = '{}_{}'.format(study._pvobj.subj_id,study._pvobj.study_id)
        if scan_id:
            output_fname = '{}-{}-{}'.format(output, scan_id, reco_id)
            try:
                study.save_as(scan_id, reco_id, output_fname)
                if args.bids:
                    study.save_json(scan_id, reco_id, output_fname)
                print('NifTi file is genetared... [{}]'.format(output_fname))
            except Exception as e:
                print('[Warning]::{}'.format(e))
        else:
            for scan_id, recos in study._pvobj.avail_reco_id.items():
                for reco_id in recos:
                    output_fname = '{}-{}-{}'.format(output, str(scan_id).zfill(2), reco_id)
                    try:
                        study.save_as(scan_id, reco_id, output_fname)
                        if args.bids:
                            study.save_json(scan_id, reco_id, output_fname)
                        print('NifTi file is genetared... [{}]'.format(output_fname))
                    except Exception as e:
                        print('[Warning]::{}'.format(e))

    elif args.function == 'tonii_all':
        path = args.path
        from os.path import join as opj, isdir, isfile
        list_of_raw = sorted([d for d in os.listdir(path) if isdir(opj(path, d)) \
                              or (isfile(opj(path, d)) and (('zip' in d) or ('PvDataset' in d)))])
        base_path = 'Data'
        try:
            os.mkdir(base_path)
        except:
            pass
        for raw in list_of_raw:
            sub_path = os.path.join(path, raw)
            study = BrukerLoader(sub_path)
            if len(study._pvobj.avail_scan_id):
                subj_path = os.path.join(base_path, 'sub-{}'.format(study._pvobj.subj_id))
                try:
                    os.mkdir(subj_path)
                except:
                    pass
                sess_path = os.path.join(subj_path, 'ses-{}'.format(study._pvobj.study_id))
                try:
                    os.mkdir(sess_path)
                except:
                    pass
                for scan_id, recos in study._pvobj.avail_reco_id.items():
                    method = study._pvobj._method[scan_id].parameters['Method']
                    if re.search('epi', method, re.IGNORECASE) and not re.search('dti', method, re.IGNORECASE):
                        output_path = os.path.join(sess_path, 'func')
                    elif re.search('dti', method, re.IGNORECASE):
                        output_path = os.path.join(sess_path, 'dwi')
                    elif re.search('flash', method, re.IGNORECASE) or re.search('rare', method, re.IGNORECASE):
                        output_path = os.path.join(sess_path, 'anat')
                    else:
                        output_path = os.path.join(sess_path, 'etc')
                    try:
                        os.mkdir(output_path)
                    except:
                        pass
                    filename = 'sub-{}_ses-{}_{}'.format(study._pvobj.subj_id, study._pvobj.study_id,
                                                         str(scan_id).zfill(2))
                    for reco_id in recos:
                        output_fname = os.path.join(output_path, '{}_reco-{}'.format(filename,
                                                                                     str(reco_id).zfill(2)))
                        try:
                            study.save_as(scan_id, reco_id, output_fname)
                            if args.bids:
                                study.save_json(scan_id, reco_id, output_fname)
                            if re.search('dti', method, re.IGNORECASE):
                                study.save_bdata(scan_id, reco_id, output_fname)
                        except Exception as e:
                            print(e)
                print('{} is converted...'.format(raw))
            else:
                print('{} is empty...'.format(raw))

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
