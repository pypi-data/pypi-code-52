# -*- coding: utf-8 -*-
# Copyright (c) 2020 Stephen Wasilewski
# =======================================================================
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# =======================================================================


"""Console script for hdrstats."""
from clasp import click
import clasp.click_ext as clk
import clasp.script_tools as cst
from hdrstats import hdrstats as hs
from hdrstats import image as img
import numpy as np
import re
import sys

@click.group()
@clk.shared_decs(clk.main_decs(hs.__version__))
def main(ctx, config, outconfig, configalias, inputalias):
    """Console script for hdrstats."""
    clk.get_config(ctx, config, outconfig, configalias, inputalias)


@main.command()
@click.argument('arg1', callback=clk.are_files)
@click.option('--hblur/--no-hblur', default=False,
              help='apply human blur before processing')
@clk.shared_decs(clk.command_decs(hs.__version__))
def img_cr(ctx, arg1, **kwargs):
    """get illuminance and contrast data from images 
    (assumes all images are the same size and view parameters)"""
    if kwargs['opts']:
        kwargs['opts'] = False
        clk.echo_args(arg1, **kwargs)
    else:
        try:
            x, y = img.img_size(arg1[0])
            cos = img.get_cos(x)
            omegas = img.get_omegas(arg1[0], x ,y)
            kws = dict(res=x, omegas=omegas, cos=cos, hblur=kwargs['hblur'])
            results = cst.pool_call(img.img_2_stats, arg1, kws)
            for i, a, r in zip(range(len(arg1)),arg1, results):
                try:
                    label = int(re.sub(r'\D', '', a))
                except ValueError:
                    label = i
                print(label, r[0], r[1])
        except click.Abort:
            raise
        except Exception as ex:
            clk.print_except(ex, kwargs['debug'])
    return 'img-cr', kwargs, ctx


@main.command()
@click.argument('arg1', callback=clk.are_files)
@click.option('-out', help='basename of output')
@click.option('-values', callback=clk.split_str, default='T1 T2 dgp E_v ugr',
              help="which values to report, can be: 'dgp', 'av_lum', 'E_v',"
              "'lum_backg', 'E_v_dir', 'dgi', 'ugr', 'vcp', 'cgi', "
              "'lum_sources', 'omega_sources', 'Lveil', 'Lveil_cie', 'dgr', "
              "'ugp', 'ugr_exp', 'dgi_mod', 'av_lum_pos', 'av_lum_pos2', "
              "'med_lum', 'med_lum_pos', 'med_lum_pos2', 'T1', 'T2'"
              "T1/T2 compute the Ev and contrast terms of DGP")
@click.option('-srcvalues', callback=clk.split_str, default=' ',
              help="which values to report for each source, can be: 'pixels',"
              " 'x-pos', 'y-pos', 'L_s', 'Omega_s', 'Posindx', 'L_b', 'L_t', "
              "'E_vert', 'Edir', 'Max_Lum', 'Sigma', 'xdir', 'ydir', 'zdir', "
              "'Eglare_cie', 'Lveil_cie', 'teta', 'glare_zone'")
@clk.shared_decs(clk.command_decs(hs.__version__))
def evalglare(ctx, arg1, **kwargs):
    """run evalglare for set of image and extract specific values"""
    if kwargs['opts']:
        kwargs['opts'] = False
        clk.echo_args(arg1, **kwargs)
    else:
        try:
            out = kwargs['out']
            results = cst.pool_call(img.evalglare, arg1)
            imgkeys = []
            for i,a in enumerate(arg1):
                try:
                    imgkeys.append(int(re.sub(r'\D', '', a)))
                except ValueError:
                    imgkeys.append(i)
            headers = dict(srcvalues=['img', 'src'], values=['img'])
            for val in ['srcvalues', 'values']:
                if len(kwargs[val]) > 0:
                    if out is  None:
                        f = sys.stdout
                    else:
                        f = open(f'{out}_{val}.txt', 'w')
                    pline = '\t'.join([f'{i: <15}' for i in headers[val] +
                                      kwargs[val]])
                    print(pline, file=f)
                    for j in range(len(arg1)):
                        if val == 'srcvalues':
                            for k, src in enumerate(results[j]['srcs']):
                                r = [imgkeys[j], k] + [src[m] for m in 
                                                       kwargs['srcvalues']]
                                pline = '\t'.join([f'{i: <15}' for i in r])
                                print(pline, file=f)
                        else:
                            r = [imgkeys[j]] + [results[j][m] for m in
                                                kwargs['values']]
                            pline = '\t'.join([f'{i: <15}' for i in r])
                            print(pline, file=f)
                    if out is not None:
                        f.close()
                    else:
                        print()
        except click.Abort:
            raise
        except Exception as ex:
            clk.print_except(ex, kwargs['debug'])
    return 'evalglare', kwargs, ctx


@main.command()
@click.argument('arg1', callback=clk.is_file)
@click.option('-idx', default=0,
              help='column to build kde from')
@click.option('-resample', callback=clk.split_float)
@clk.shared_decs(clk.command_decs(hs.__version__))
def kde(ctx, arg1, **kwargs):
    """generate KDE for samples"""
    
    if kwargs['opts']:
        kwargs['opts'] = False
        clk.echo_args(arg1, arg2, outpref, **kwargs)
    else:
        try:
            aS = np.loadtxt(arg1)[:,kwargs['idx']]
            ssize = hs.kde_cont(aS, kwargs['resample'])
            for i in ssize:
                print(i[0], i[1])
        except click.Abort:
            raise
        except Exception as ex:
            clk.print_except(ex, kwargs['debug'])
    return 'kde', kwargs, ctx


@main.command()
@click.argument('arg1', callback=clk.is_file)
@click.argument('arg2', callback=clk.is_file)
@click.argument('outpref')
@click.option('-sidx', default=0,
              help='first column of data (to exclude labels)')
@click.option('-baselinei', type=int,
              help='use i as baseline for KDE of all columns')
@click.option('-resample', callback=clk.split_float)
@click.option('--dototal/--no-dototal', default=False)
@click.option('--legacy/--no-legacy', default=False)
@click.option('-rng', default=None, callback=clk.split_int)
@clk.shared_decs(clk.command_decs(hs.__version__))
def kde_error(ctx, arg1, arg2, outpref, **kwargs):
    """calculate error between 2 2D data files using gaussian KDE"""
    
    def get_baseline(aS, i, maxN=10000):
        if i < aS.shape[-1]:
            a = aS[:,i]
        else:
            a = aS.flatten()
        la = len(a)
        if la > maxN:
            scale = la/maxN
            select = np.random.randint(la, size=maxN)
            a = a[select]
        else:
            scale = 1
            select = None
        b = a
        if np.max(b) > 30:
            baseline = np.log10(b)
        else:
            print('NO LOG CORRECTION')
            baseline = b
        return baseline, scale, select


    def get_rdif(aS, a2S, i, select=None):
        if i < aS.shape[-1]:
            a = np.stack((aS[:,i],a2S[:,i])).T
        else:
            a = np.stack((aS.flatten(),a2S.flatten())).T
        la = len(a)
        if select is not None:
            scale = la/maxN
        b = a
        return b[:,1]/b[:,0] - 1
    
    if kwargs['opts']:
        kwargs['opts'] = False
        clk.echo_args(arg1, arg2, outpref, **kwargs)
    else:
        try:
            aS = np.loadtxt(arg1)
            a2S = np.loadtxt(arg2)[:,kwargs['sidx']:]
            labels = aS[:,0]
            aS = aS[:,kwargs['sidx']:]
            if kwargs['baselinei'] is not None:
                baseline, scale, select = get_baseline(aS, kwargs['baselinei']
                                                       - kwargs['sidx'])
            if kwargs['rng'] is None:
                srng = range(aS.shape[-1] + kwargs['dototal'])
            else:
                srng = np.array(kwargs['rng']) - kwargs['sidx']
            for i in srng:
                if kwargs['baselinei'] is None:
                    baseline, scale, select = get_baseline(aS, i)
                rdif = get_rdif(aS, a2S, i, select)
                adif = np.abs(rdif)
                out = hs.error_cont(baseline, adif, rdif, scale=scale,
                                  resample=kwargs['resample'])
                ti = i + kwargs['sidx']
                outf = f'{outpref}_{ti}.txt'
                if kwargs['legacy']:
                    if kwargs['resample'] is None:
                        out = np.hstack((labels.reshape(-1, 1), out[:,0:-1],
                                        rdif.reshape(-1, 1),
                                        adif.reshape(-1, 1)))
                    else:
                        out = np.hstack((out[:,0:1], out))
                np.savetxt(outf, out)
        except click.Abort:
            raise
        except Exception as ex:
            clk.print_except(ex, kwargs['debug'])
    return 'kde-error', kwargs, ctx


@main.command()
@click.argument('dataf', callback=clk.are_files)
@click.option('-x_vals', default="0,0",
              callback=clk.tup_int, help="index for xvals")
@click.option('-y_vals', default="-1", callback=clk.tup_int,
              help="index for yvals")
@click.option('--header/--no-header', default=False,
              help="indicates that data has a header row to get "
              "series labels (overridden by labels)")
@click.option('--xheader/--no-xheader', default=False,
              help="indicates that data has a header column to get x-axis "
              "labels (overridden by xlabels)")
@click.option('--rows/--no-rows', default=False,
              help="get data rows instead of columns")
@click.option('--lin/--no-lin', default=False,
              help="linear regression (r^2)")
@click.option('--spearman/--no-spearman', default=True)
@click.option('--pearson/--no-pearson', default=True)
@click.option('--pvals/--no-pvals', default=False)
@click.option('-drange', callback=clk.split_int,
              help="index range for data series, if None gets all")
@click.option('--weatherfile/--no-weatherfile', default=False,
              help="input files will be read as weather files: "
              "0 month, 1 day, 2 hour, 3 dirnorn, 4 difhoriz, 5 "
              "globhoriz, 6 skycover")
@click.option('-labels', callback=clk.split_str,
              help="input custom series labels, by default uses "
              "file name and index or --header option")
@click.option('--opts','-opts', is_flag=True,
              help="check parsed options")
@click.option('--debug', is_flag=True,
              help="show traceback on exceptions")
def corr(dataf, **kwargs):
    '''
    compute statistics between pairs of data
    '''
    if kwargs['opts']:
        kwargs['opts'] = False
        clk.echo_args(dataf, **kwargs)
    else:
        try:
            a1 = cst.kwarg_match(cst.read_data, kwargs)
            outs = [hs.corr_header(**kwargs)]
            # print(f"series\t{hl}")
            xs, ys, l2 = cst.read_all_data(dataf, **a1)
            if kwargs['labels'] is None:
                labels = l2
            else:
                labels = kwargs['labels']
            nlab = len(labels)
            for i in range(len(ys)):
                if i >= nlab:
                    labels.append("series{:02d}".format(i))
            results = cst.pool_call(hs.corr_calc, zip(xs, ys), expand=True,
                                    kwargs=kwargs)
            outs += [[f'{i:.04f}' for i in r] for r in results]
            ot = np.array(outs).T
            print('\t'.join([f'{i: <20}' for i in ['stat'] + labels]))
            for i in ot:
                print('\t'.join([f'{j: <20}' for j in i]))
        except click.Abort:
            raise
        except Exception as ex:
            clk.print_except(ex, kwargs['debug'])
    return 'corr', kwargs


# @main.command()
# @click.argument('arg1')
# @clk.shared_decs(clk.command_decs(hs.__version__))
# def XXX(ctx, arg1, **kwargs):
#     """callbacks for special parsing of command line inputs
#
# Callbacks By type
# -----------------
#
# File input
# ~~~~~~~~~~
#
# file inputs can be given with wildcard expansion (in quotes so that the
# callback handles) using glob plus the following:
#
#     * [abc] (one of a, b, or c)
#     * [!abc] (none of a, b or c)
#     * '-' (hyphen) collect the stdin into a temporary file (clasp_tmp*)
#     * ~ expands user
#
# callback functions:
#
#     * is_file: check if a single path exists (prompts for user input if file
#       not found)
#     * are_files: recursively calls parse_file_list and prompts on error
#     * is_file_iter: use when multiple=True
#     * are_files_iter: use when mulitple=True
#     * are_files_or_str: tries to parse as files, then tries split_float, then
#       split_int, then returns string
#     * are_files_or_str_iter: use when mulitple=True
#
# String parsing
# ~~~~~~~~~~~~~~
#
#     * split_str: split with shlex.split
#     * split_str_iter: use when multiple=True
#     * color_inp: return alpha string, split on whitespace,
#       convert floats and parse tuples on ,
#
# Number parsing
# ~~~~~~~~~~~~~~
#
#     * tup_int: parses integer tuples from comma/space separated string
#     * tup_float: parses float tuples from comma/space separated string
#     * split_float: splits list of floats and extends ranges based on : notation
#     * split_int: splits list of ints and extends ranges based on : notation
# """
#     if kwargs['opts']:
#         kwargs['opts'] = False
#         clk.echo_args(arg1, **kwargs)
#     else:
#         try:
#             pass
#         except click.Abort:
#             raise
#         except Exception as ex:
#             clk.print_except(ex, kwargs['debug'])
#     return 'XXX', kwargs, ctx




@main.resultcallback()
@click.pass_context
def printconfig(ctx, opts, **kwargs):
    """callback to save config file"""
    try:
        clk.tmp_clean(opts[2])
    except Exception:
        pass
    if kwargs['outconfig']:
        clk.print_config(ctx, opts, kwargs['outconfig'], kwargs['config'],
                         kwargs['configalias'])


if __name__ == '__main__':
    main()
