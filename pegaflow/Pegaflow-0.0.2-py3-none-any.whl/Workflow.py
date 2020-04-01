#!/usr/bin/env python3
"""
Class Workflow is a class for other programs to inherit and helps to simplify pegasus workflow dax writing.
"""
import sys, os
from . DAX3 import Executable, File, PFN, Profile, Namespace, Link, ADAG, Use, Job, Dependency

src_dir = os.path.dirname(os.path.abspath(__file__))

class PassingData(object):
    """
    a class to hold any data structure
    """
    def __init__(self, **keywords):
        """
        add keyword handling
        """
        for argument_key, argument_value in keywords.items():
            setattr(self, argument_key, argument_value)
    
    def __str__(self):
        """
        a string-formatting function
        """
        return_ls = []
        for attributeName in dir(self):
            if attributeName.find('__')==0:	#ignore the 
                continue
            value = getattr(self, attributeName, None)
            return_ls.append("%s = %s"%(attributeName, value))
            
        return ", ".join(return_ls)
    
    def __getitem__(self, key):
        """
        enable it to work like a dictionary
            i.e. pdata.chromosome or pdata['chromosome'] is equivalent if attribute 0 is chromosome.
        """
        return self.__getattribute__(key)

def getListOutOfStr(list_in_str=None, data_type=int, separator1=',', separator2='-'):
    """
    This function parses a list from a string representation of a list, such as '1,3-7,11'=[1,3,4,5,6,7,11].
    If only separator2, '-', is used ,all numbers have to be integers.
    If all are separated by separator1, it could be in non-int data_type.
    strip the strings as much as u can.
    if separator2 is None or nothing or 0, it wont' be used.

    Examples:
        self.chromosomeList = utils.getListOutOfStr('1-5,7,9', data_type=str, separator2=None)
    """
    list_to_return = []
    if list_in_str=='' or list_in_str is None:
        return list_to_return
    list_in_str = list_in_str.strip()
    if list_in_str=='' or list_in_str is None:
        return list_to_return
    if type(list_in_str)==int:	#just one integer, put it in and return immediately
        return [list_in_str]
    index_anchor_ls = list_in_str.split(separator1)
    for index_anchor in index_anchor_ls:
        index_anchor = index_anchor.strip()
        if len(index_anchor)==0:	#nothing there, skip
            continue
        if separator2:
            start_stop_tup = index_anchor.split(separator2)
        else:
            start_stop_tup = [index_anchor]
        if len(start_stop_tup)==1:
            list_to_return.append(data_type(start_stop_tup[0]))
        elif len(start_stop_tup)>1:
            start_stop_tup = map(int, start_stop_tup)
            list_to_return += range(start_stop_tup[0], start_stop_tup[1]+1)
    list_to_return = map(data_type, list_to_return)
    return list_to_return

def getRealPrefixSuffixOfFilenameWithVariableSuffix(path, fakeSuffix='.gz', fakeSuffixSet = set(['.gz', '.zip', '.bz2', '.bz'])):
    """
    The purpose of this function is to get the prefix, suffix of a filename regardless of whether it
        has two suffices (gzipped) or one. 
    i.e.
        A file name is either sequence_628BWAAXX_4_1.fastq.gz or sequence_628BWAAXX_4_1.fastq (without gz).
        This function returns ('sequence_628BWAAXX_4_1', '.fastq')

    "." is considered part of the filename suffix.
    """
    fname_prefix, fname_suffix =  os.path.splitext(path)
    if fakeSuffix and fakeSuffix not in fakeSuffixSet:
        fakeSuffixSet.add(fakeSuffix)
    while fname_suffix in fakeSuffixSet:
        fname_prefix, fname_suffix =  os.path.splitext(fname_prefix)
    return fname_prefix, fname_suffix


def addMkDirJob(workflow=None, mkdir=None, outputDir=None, namespace=None, version=None,\
            parentJobLs=None, extraDependentInputLs=None):
    """
    """
    # Add a mkdir job for any directory.
    job = Job(namespace=getattr(workflow, 'namespace', namespace), name=mkdir.name, \
                version=getattr(workflow, 'version', version))
    job.addArguments(outputDir)
    job.folder = outputDir	#custom attribute
    job.output = outputDir	#custom attribute
    workflow.addJob(job)
    if parentJobLs:
        for parentJob in parentJobLs:
            if parentJob:
                workflow.depends(parent=parentJob, child=job)
    if extraDependentInputLs:
        for input in extraDependentInputLs:
            if input is not None:
                job.uses(input, transfer=True, register=True, link=Link.INPUT)
    if hasattr(workflow, 'no_of_jobs'):
        workflow.no_of_jobs += 1
    return job

def setJobResourceRequirement(job=None, job_max_memory=500, no_of_cpus=1, walltime=180, sshDBTunnel=0):
    """
    job_max_memory: integer, unit in MB.
        if job_max_memory is None, then skip setting memory requirement.
        if job_max_memory is "" or 0 or "0", then assign 500 (MB) to it.
    sshDBTunnel:
        =1: this job needs a ssh tunnel to access an external database server.
        =anything else: no need for that.
    walltime: integer, unit in minutes.
        set walltime default to 180 minutes (3 hours).
    """
    condorJobRequirementLs = []
    if job_max_memory == "" or job_max_memory == 0 or job_max_memory =="0":
        job_max_memory = 500
    if job_max_memory is not None: 
        job.addProfile(Profile(Namespace.GLOBUS, key="maxmemory", value="%s"%(job_max_memory)))
        job.addProfile(Profile(Namespace.CONDOR, key="request_memory", value="%s"%(job_max_memory)))	#for dynamic slots
        condorJobRequirementLs.append("(memory>=%s)"%(job_max_memory))
    if sshDBTunnel==1:
        condorJobRequirementLs.append("(sshDBTunnel==%s)"%(sshDBTunnel))	#use ==, not =.
    
    if no_of_cpus is not None:
        job.addProfile(Profile(Namespace.CONDOR, key="request_cpus", value="%s"%(no_of_cpus)) )	#for dynamic slots
    
    if walltime is not None:
        #scale walltime according to cluster_size
        job.addProfile(Profile(Namespace.GLOBUS, key="maxwalltime", value="%s"%(walltime)) )
        #TimeToLive is in seconds
        condorJobRequirementLs.append("(Target.TimeToLive>=%s)"%(int(walltime)*60) )
    #key='requirements' could only be added once for the condor profile
    job.addProfile(Profile(Namespace.CONDOR, key="requirements", value=" && ".join(condorJobRequirementLs) ))

def registerFile(workflow, filepath):
    """
    function to register any file to the workflow.input_site_handler, 
    """
    file = File(os.path.basename(filepath))
    file.addPFN(PFN("file://" + os.path.abspath(filepath), \
                                workflow.input_site_handler))
    workflow.addFile(file)
    return file

def getAbsPathOutOfExecutable(executable):
    """
        This function extracts path out of a registered executable.
            executable is a registered pegasus executable with PFNs.
    """
    pfn = (list(executable.pfns)[0])
    #the url looks like "file:///home/crocea/bin/bwa"
    return pfn.url[7:]


def getAbsPathOutOfFile(file):
    """
    call getAbsPathOutOfExecutable
    """
    return getAbsPathOutOfExecutable(file)

def getExecutableClusterSize(executable=None):
    """
    default is None
    """
    cluster_size = None
    clusteringProf = Profile(Namespace.PEGASUS, key="clusters.size", value="1")
    for profile in executable.profiles:
        if clusteringProf.__hash__() == profile.__hash__():	#__hash__ only involves namespace + key 
            cluster_size = profile.value
    return cluster_size


class Workflow(ADAG):
    __doc__ = __doc__
    # Each entry of pathToInsertHomePathList should contain %s, i.e. '%s/bin/myprogram'
    #  and will be expanded to be '/home/user/bin/myprogram'.
    # Child classes can add stuff into this list.
    pathToInsertHomePathList = []
    def __init__(self, inputSuffixList=None, \
            pegasusFolderName='folder', output_path=None, \
            site_handler=None, input_site_handler=None, cluster_size=1, \
            tmpDir='/tmp/', max_walltime=4320, \
            javaPath=None, jvmVirtualByPhysicalMemoryRatio=1.2,\
            debug=False, needSSHDBTunnel=False, report=False):
        """
        site_handler: The name of the computing site where the jobs run and executables are stored. Check your Pegasus configuration.
        input_site_handler: 'local or same as site_handler. It is the name of the site that has all the input files.'
            'If it is the same as site_handler, the input files will be symlinked.'
            'If input_site_handler=local, input files will be transferred to the computing cluster by pegasus-transfer.'
        cluster_size: 'The number of pegasus jobs that should be clustered into one job. '
            'Good if your workflow contains many quick jobs. It will reduce Pegasus monitor I/O.'
        pegasusFolderName: 'the path relative to the pegasus workflow root. This folder will contains pegasus input & output.'
            'It will be created during the pegasus staging process. It is useful to separate multiple sub-workflows.'
            'If empty or None, everything is in the pegasus root.'
        inputSuffixList: 'coma-separated list of input file suffices. If None, any suffix.'
            'Suffix include the dot, (i.e. .tsv). Typical zip suffices are excluded (.gz, .bz2, .zip, .bz).'
        output_path: 'the path to the output file that will contain the Pegasus DAG.'
        tmpDir: 'a local folder for some jobs (MarkDup) to store temp data. /tmp/ can be too small sometimes.'
        max_walltime: 'maximum wall time any job could have, in minutes. 20160=2 weeks.'
            'used in addGenericJob().'
        jvmVirtualByPhysicalMemoryRatio: "if a job's virtual memory (usually 1.2X of JVM resident memory) exceeds request, "
            "it will be killed on some clusters, hoffman2. This will make sure your job requests enough memory from the job scheduler."
        debug: 'toggle debug mode.'
        needSSHDBTunnel: 'If all DB-interacting jobs need a ssh tunnel to access a database that is inaccessible to computing nodes.'
        report: 'toggle verbose output.'
        """
        self.inputSuffixList = getListOutOfStr(list_in_str=inputSuffixList, data_type=str, 
            separator1=',', separator2='-')
        self.inputSuffixSet = set(self.inputSuffixList)
        self.pegasusFolderName = pegasusFolderName
        self.output_path = output_path
        self.site_handler = site_handler
        self.input_site_handler = input_site_handler
        if not self.input_site_handler:
            self.input_site_handler = self.site_handler
        self.cluster_size = cluster_size
        self.tmpDir = tmpDir
        self.max_walltime = max_walltime
        self.javaPath = javaPath
        self.jvmVirtualByPhysicalMemoryRatio = jvmVirtualByPhysicalMemoryRatio
        self.debug = debug
        self.needSSHDBTunnel = needSSHDBTunnel
        self.report = report
        #change the workflow name to reflect the output filename
        workflowName = os.path.splitext(os.path.basename(self.output_path))[0]
        # call parent
        self.name = workflowName
        ADAG.__init__(self, self.name)

        for pathName in self.pathToInsertHomePathList:
            absPath = self.insertHomePath(getattr(self, pathName, None), self.home_path)
            if absPath:
                setattr(self, pathName, absPath)
            else:
                sys.stderr.write("Warning: %s has an empty absolute path. Skip.\n"%(pathName))
        
        self.architecture = "x86_64"
        self.operatingSystem = "linux"
        self.namespace = "pegasus"
        self.version="1.0"

        self.commandline = ' '.join(sys.argv)

        #global counter
        self.no_of_jobs = 0
        #flag to check if dag has been outputted or not
        self.isDAGWrittenToDisk = False

        self.extra__init__()	#this must be ahead of connectDB().
        self.connectDB()

    def extra__init__(self):
        """
        placeholder
        """
        pass

    def writeXML(self, out):
        """
        Write the ADAG as XML to a stream.
        Overwrite its parent: ADAG.writeXML().
        check self.isDAGWrittenToDisk first.
        call ADAG.writeXML() and then add my commandline comment.
        """
        if self.isDAGWrittenToDisk:
            print("Warning: the dag has been written to a file already (writeXML() has been called). No more calling.", flush=True)
        else:
            print(f"Writing XML job to {out} ... ", flush=True, end='')
            ADAG.writeXML(self, out)
            # -- is not allowed in xml.
            out.write('<!-- commandline: %s -->\n'%(self.commandline.replace("--", "~~")))
            print("Done", flush=True)
            self.isDAGWrittenToDisk = True
    
    def constructOneExecutableObject(self, path=None, name=None, checkPathExecutable=True, version=None, namespace=None,\
                                    noVersion=False):
        """
        check if path is an executable file.
        """
        if not namespace:
            namespace = self.namespace
        if not version:
            version = self.version
        operatingSystem = self.operatingSystem
        architecture = self.architecture
        site_handler = self.site_handler

        if noVersion:
            #removed argument version from Executable()
            executable = Executable(namespace=namespace, name=name,\
                        os=operatingSystem, arch=architecture, installed=True)
        else:
            executable = Executable(namespace=namespace, name=name, version=version,\
                        os=operatingSystem, arch=architecture, installed=True)
        #
        if checkPathExecutable:
            if path.find('file://')==0:
                fs_path = path[6:]
            else:
                fs_path = path
            
            if not (os.path.isfile(fs_path) and os.access(fs_path, os.X_OK)):
                sys.stderr.write("Error from constructOneExecutableObject(): \
        executable %s is not an executable.\n"%(path))
                raise
        executable.addPFN(PFN("file://" + os.path.expanduser(path), site_handler))
        return executable

    def connectDB(self):
        """
        placeholder, to establish db connection
        """
        self.db_main = None

    def insertHomePath(self, inputPath, home_path):
        """
        inputPath could be None
        """
        if inputPath:
            if inputPath.find('%s')!=-1:
                inputPath = inputPath%home_path
        else:
            inputPath = None
        return inputPath

    def registerJars(self):
        """
        register jars to be used in the workflow
        """
        pass

    def registerCustomJars(self):
        """
        custom jars specific to the workflow, not for child classes to have.
        """
        pass

    def registerCustomExecutables(self):
        """
        custom executable specific to the workflow, not for child classes to have.
        """
        pass


    def registerExecutables(self):
        """
        """
        if hasattr(self, 'javaPath') and self.javaPath:
            self.addExecutableFromPath(path=self.javaPath, name='java', clusterSizeMultipler=1)
        self.addExecutableFromPath(path="/bin/cp", name='cp', clusterSizeMultipler=1)
        self.addExecutableFromPath(path="/bin/mv", name='mv', clusterSizeMultipler=1)
        self.addExecutableFromPath(path=os.path.join(src_dir, "shell/runShellCommand.sh"), \
                name='runShellCommand', clusterSizeMultipler=1)
        self.addExecutableFromPath(path=os.path.join(src_dir, 'shell/pipeCommandOutput2File.sh'), \
                name='pipeCommandOutput2File', clusterSizeMultipler=1)
        self.addExecutableFromPath(path=os.path.join(src_dir, 'shell/sortHeaderAware.sh'), \
                name='sortHeaderAware', clusterSizeMultipler=1)
        #to be used on pipeCommandOutput2File.sh
        self.sortExecutableFile = self.registerOneExecutableAsFile(path="/usr/bin/sort")
        #mkdirWrap is different from mkdir that it doesn't report error when the directory is already there.
        self.addExecutableFromPath(path=os.path.join(src_dir, 'shell/mkdirWrap.sh'), \
                                        name='mkdirWrap', clusterSizeMultipler=1)
        self.addExecutableFromPath(path=os.path.join(src_dir, "shell/gzip.sh"), 
            name='gzip', clusterSizeMultipler=1)
        
    def setExecutablesClusterSize(self, executableClusterSizeMultiplierList=[], defaultClusterSize=None):
        """
        make sure the profile of clusters.size is not added already.
        """
        if defaultClusterSize is None:
            defaultClusterSize = self.cluster_size
        for executableClusterSizeMultiplierTuple in executableClusterSizeMultiplierList:
            executable = executableClusterSizeMultiplierTuple[0]
            if len(executableClusterSizeMultiplierTuple)==1:
                clusterSizeMultipler = 1
            else:
                clusterSizeMultipler = executableClusterSizeMultiplierTuple[1]
            self.setExecutableClusterSize(executable=executable, \
                clusterSizeMultipler=clusterSizeMultipler, defaultClusterSize=defaultClusterSize)
    
    def setExecutableClusterSize(self, executable=None, clusterSizeMultipler=1, defaultClusterSize=None):
        """
        it will remove the clustering profile if the new clusterSize is <1
        """
        if defaultClusterSize is None:
            defaultClusterSize = self.cluster_size
        clusterSize = int(defaultClusterSize*clusterSizeMultipler)
        clusteringProf = Profile(Namespace.PEGASUS, key="clusters.size", value="%s"%clusterSize)
        if executable.hasProfile(clusteringProf):
            executable.removeProfile(clusteringProf)
        if clusterSize>1:
            executable.addProfile(clusteringProf)
        if not self.hasExecutable(executable):
            self.addExecutable(executable)	#removeExecutable() is its counterpart
            setattr(self, executable.name, executable)
        return executable

    def addExecutableFromPath(self, path=None, name=None, clusterSizeMultipler=1, noVersion=False):
        """
        combination of constructOneExecutableObject() & setExecutableClusterSize()
        """
        if clusterSizeMultipler is None:
            clusterSizeMultipler = 1
        executable = self.constructOneExecutableObject(path=path, name=name, noVersion=noVersion)
        self.setExecutableClusterSize(executable=executable, clusterSizeMultipler=clusterSizeMultipler)
        return executable

    def getExecutableClusterSize(self, executable=None):
        """
        default is None
        """
        return getExecutableClusterSize(executable)

    def getFilesWithProperSuffixFromFolder(self, inputFolder=None, suffix='.h5'):
        """
        """
        sys.stderr.write("Getting files with %s as suffix from %s ..."%(suffix, inputFolder))
        inputFnameLs = []
        counter = 0
        for filename in os.listdir(inputFolder):
            prefix, file_suffix = os.path.splitext(filename)
            counter += 1
            if file_suffix==suffix:
                inputFnameLs.append(os.path.join(inputFolder, filename))
        sys.stderr.write("%s files out of %s total.\n"%(len(inputFnameLs), counter))
        return inputFnameLs

    def getFilesWithSuffixFromFolderRecursive(self, inputFolder=None, suffixSet=set(['.h5']), fakeSuffix='.gz', inputFnameLs=[]):
        """
        similar to getFilesWithProperSuffixFromFolder() but recursively go through all sub-folders
            and it uses utils.getRealPrefixSuffixOfFilenameWithVariableSuffix() to get the suffix.
        """
        sys.stderr.write("Getting files with %s as suffix (%s as fake suffix) from %s ...\n"%(repr(suffixSet), fakeSuffix, inputFolder))
        counter = 0
        for filename in os.listdir(inputFolder):
            inputFname = os.path.join(inputFolder, filename)
            counter += 1
            if os.path.isfile(inputFname):
                prefix, file_suffix = getRealPrefixSuffixOfFilenameWithVariableSuffix(filename, fakeSuffix=fakeSuffix)
                if file_suffix in suffixSet:
                    inputFnameLs.append(inputFname)
            elif os.path.isdir(inputFname):
                self.getFilesWithSuffixFromFolderRecursive(inputFname, suffixSet=suffixSet, \
                    fakeSuffix=fakeSuffix, inputFnameLs=inputFnameLs)
        sys.stderr.write("%s files out of %s total.\n"%(len(inputFnameLs), counter))
        #return inputFnameLs

    def registerFilesOfInputDir(self, inputDir=None,  inputFnameLs=None, input_site_handler=None, \
                pegasusFolderName='', inputSuffixSet=None, indexFileSuffixSet=set(['.tbi', '.fai']),\
                **keywords):
        """
        This function registers all files in inputDir (if present) and inputFnameLs (if not None).
        indexFileSuffixSet is used to add additional index files related to an input file.
            assuming index file name is original filename + indexFileSuffix.
        """
        if inputFnameLs is None:
            inputFnameLs = []
        if inputDir and os.path.isdir(inputDir):
            fnameLs = os.listdir(inputDir)
            for fname in fnameLs:
                inputFname = os.path.realpath(os.path.join(inputDir, fname))
                inputFnameLs.append(inputFname)

        if inputSuffixSet is None:
            inputSuffixSet = self.inputSuffixSet
        print(f"Registering {len(inputFnameLs)} input files with suffix in {inputSuffixSet} ... ", \
            flush=True, end='')
        returnData = PassingData(jobDataLs = [])
        counter = 0
        for inputFname in inputFnameLs:
            counter += 1
            suffix = getRealPrefixSuffixOfFilenameWithVariableSuffix(inputFname)[1]	#default fakeSuffixSet includes .gz
            if inputSuffixSet is not None and len(inputSuffixSet)>0 and suffix not in inputSuffixSet:
                #skip input whose suffix is not in inputSuffixSet if inputSuffixSet is a non-empty set.
                continue
            if indexFileSuffixSet is not None and len(indexFileSuffixSet)>0 and suffix in indexFileSuffixSet:
                #skip index files, they are affiliates of real input data files.
                continue
            inputFile = File(os.path.join(pegasusFolderName, os.path.basename(inputFname)))
            inputFile.addPFN(PFN("file://" + inputFname, input_site_handler))
            inputFile.abspath = inputFname
            self.addFile(inputFile)
            jobData = PassingData(output=inputFile, job=None, jobLs=[], \
                                file=inputFile, fileLs=[inputFile], indexFileLs=[])
            #find all index files.
            for indexFileSuffix in indexFileSuffixSet:
                indexFilename = '%s%s'%(inputFname, indexFileSuffix)
                if os.path.isfile(indexFilename):
                    indexFile = self.registerOneInputFile(inputFname=indexFilename, \
                                    input_site_handler=input_site_handler, folderName=pegasusFolderName, \
                                    useAbsolutePathAsPegasusFileName=False, checkFileExistence=True)
                    jobData.fileLs.append(indexFile)
                    jobData.indexFileLs.append(indexFile)
            returnData.jobDataLs.append(jobData)
        print(f"{len(returnData.jobDataLs)} out of {len(inputFnameLs)} possible files registered. Done.", flush=True)
        return returnData

    def registerFilesAsInputToJob(self, job, inputFileList):
        """
        call addJobUse()
        """
        for inputFile in inputFileList:
            self.addJobUse(job=job, file=inputFile, transfer=True, register=True, link=Link.INPUT)
            #job.uses(inputFile, transfer=True, register=True, link=Link.INPUT)

    def registerOneInputFile(self, inputFname=None, input_site_handler=None, folderName="", \
                            useAbsolutePathAsPegasusFileName=False,\
                            pegasusFileName=None, checkFileExistence=True):
        """
        Examples:
            pegasusFile = self.registerOneInputFile(inputFname='/tmp/abc.txt')
        
        useAbsolutePathAsPegasusFileName:
            This would render the file to be referred as the absolute path on the running computer.
            And pegasus will not symlink or copy/transfer the file.
            Set it to True only if you don't want to add the file to the job as an INPUT dependency (as it's accessed through abs path).
        folderName: if given, it will cause the file to be put into that folder (relative path) within the pegasus workflow running folder.
            This folder needs to be created by a mkdir job.
        Return: pegasusFile.abspath or pegasusFile.absPath is the absolute path of the file.
        """
        if input_site_handler is None:
            input_site_handler = self.input_site_handler
        if not pegasusFileName:
            if useAbsolutePathAsPegasusFileName:
                #this will stop symlinking/transferring , and also no need to indicate them as file dependency for jobs.
                pegasusFileName = os.path.abspath(inputFname)
            else:
                pegasusFileName = os.path.join(folderName, os.path.basename(inputFname))
        pegasusFile = File(pegasusFileName)
        if checkFileExistence and not os.path.isfile(inputFname):
            sys.stderr.write("Error from registerOneInputFile(): %s does not exist.\n"%(inputFname))
            raise
        pegasusFile.abspath = os.path.abspath(inputFname)
        pegasusFile.absPath = pegasusFile.abspath
        pegasusFile.addPFN(PFN("file://" + pegasusFile.abspath, input_site_handler))
        if not self.hasFile(pegasusFile):
            # check if the file is already added to the workflow.
            self.addFile(pegasusFile)
        return pegasusFile

    def registerOneJar(self, name=None, path=None, site_handler=None, workflow=None, folderName="", useAbsolutePathAsPegasusFileName=False):
        """
        useAbsolutePathAsPegasusFileName=True if you do not plan to add a jar file as INPUT dependency for jobs
        """
        if site_handler is None:
            site_handler = self.site_handler	#usually they are same
        if not folderName:
            folderName = "jar"
        pegasusFile = self.registerOneInputFile(inputFname=path, input_site_handler=site_handler, \
                                            folderName=folderName, useAbsolutePathAsPegasusFileName=useAbsolutePathAsPegasusFileName)
        setattr(self, name, pegasusFile)
        return pegasusFile

    def registerOneExecutableAsFile(self, pythonVariableName=None, path=None, site_handler=None, \
                                folderName="", useAbsolutePathAsPegasusFileName=False):
        """
        Examples:
            self.samtoolsExecutableFile = self.registerOneExecutableAsFile(path=self.samtools_path,\
                                                    input_site_handler=self.input_site_handler)
            self.registerOneExecutableAsFile(pythonVariableName="bwaExecutableFile", path=self.bwa_path)

        pythonVariableName is used for access like self.pythonVariableName within python dag generator.
        useAbsolutePathAsPegasusFileName=True if you do not plan to add the file as INPUT dependency for jobs.
        """
        if site_handler is None:
            site_handler = self.site_handler
        if not folderName:
            folderName = "executable"
        if not pythonVariableName:
            pythonVariableName = '%sExecutableFile'%(os.path.basename(path))
        pegasusFile = self.registerOneInputFile(inputFname=path, input_site_handler=site_handler, \
                                            folderName=folderName, \
                                            useAbsolutePathAsPegasusFileName=useAbsolutePathAsPegasusFileName)
        setattr(self, pythonVariableName, pegasusFile)
        return pegasusFile

    def addInputToMergeJob(self, mergeJob=None, inputF=None, inputArgumentOption="",\
                            parentJobLs=None, \
                            extraDependentInputLs=None, **keywords):
        """
        This function adds inputF or parentJobLs[i].output (if inputF is not given) as input to mergeJob.
        inputArgumentOption (like '-i') is added in front of each input file.
        extraDependentInputLs is a list of dependent files to mergeJob,
            which will NOT be added to the commandline of mergeJob.
        i.e.
            self.addInputToMergeJob(mergeJob=mergeDataJob, inputF=input_file])
            self.addInputToMergeJob(mergeJob=gatkUnionJob, parentJobLs=[gatk_job], \
                                            inputArgumentOption="--variant")
        
        """
        if inputF is None and parentJobLs is not None:
            parentJob = parentJobLs[0]
            if hasattr(parentJob, 'output'):
                inputF = parentJob.output
        if inputF:
            isAdded = self.addJobUse(mergeJob, file=inputF, transfer=True, register=True, link=Link.INPUT)
            if isAdded:
                if inputArgumentOption:
                    #add it in front of each input file
                    mergeJob.addArguments(inputArgumentOption)
                mergeJob.addArguments(inputF)

        if extraDependentInputLs:
            for inputFile in extraDependentInputLs:
                if inputFile:
                    isAdded = self.addJobUse(mergeJob, file=inputFile, transfer=True, register=True, link=Link.INPUT)

        if parentJobLs:
            for parentJob in parentJobLs:
                if parentJob:
                    self.addJobDependency(parentJob=parentJob, childJob=mergeJob)

    def addSortJob(self, executable=None, commandFile=None, \
            inputFile=None, outputFile=None, noOfHeaderLines=0, \
            parentJobLs=None, extraDependentInputLs=None, extraOutputLs=None, transferOutput=False, \
            extraArgumentList=None, extraArguments=None, sshDBTunnel=None,\
            job_max_memory=200, walltime=120, **keywords):
        """
        use sortHeaderAware executable (from pymodule/shell).
        Examples:
            sortedSNPID2NewCoordinateFile = File(os.path.join(reduceOutputDirJob.output, 'SNPID2NewCoordinates.sorted.tsv.gz'))
            sortSNPID2NewCoordinatesJob = self.addSortJob(inputFile=reduceJob.output, \
                        outputFile=sortedSNPID2NewCoordinateFile, noOfHeaderLines=1, \
                        parentJobLs=[reduceJob], \
                        extraOutputLs=None, transferOutput=False, \
                        extraArgumentList=["-k3,3 -k4,4n"], \
                        sshDBTunnel=None,\
                        job_max_memory=4000, walltime=120)
            # -t$'\t' for sort has to be removed as it won't be passed correctly.
            # the default sort field separator (non-blank to blank) works if no-blank is part of each cell value.
        """
        if executable is None:
            executable = self.sortHeaderAware
        if commandFile is None:
        	commandFile = self.sortExecutableFile
        if extraDependentInputLs is None:
            extraDependentInputLs = []
        if extraArgumentList is None:
            extraArgumentList = []

        extraArgumentList.insert(0, "%s"%(noOfHeaderLines))
        job = self.addGenericJob(executable=executable, \
                    inputFile=inputFile, inputArgumentOption="", \
                    outputFile=outputFile, outputArgumentOption="",
                    extraOutputLs=extraOutputLs, transferOutput=transferOutput, \
                    parentJobLs=parentJobLs, \
                    extraDependentInputLs=extraDependentInputLs, \
                    extraArgumentList=extraArgumentList, \
                    extraArguments=extraArguments, \
                    sshDBTunnel=sshDBTunnel,\
                    job_max_memory=job_max_memory, walltime=walltime)
        return job
    
    def addDBJob(self, executable=None, inputFile=None, inputArgumentOption="-i", \
                    inputFileList=None, argumentForEachFileInInputFileList=None,\
                    outputFile=None, outputArgumentOption="-o", \
                    parentJobLs=None, extraDependentInputLs=None, extraOutputLs=None, transferOutput=False, \
                    extraArguments=None, extraArgumentList=None, job_max_memory=200,  sshDBTunnel=None, \
                    key2ObjectForJob=None, objectWithDBArguments=None, walltime=None, **keywords):
        """
        similar to addGenericJob but these are jobs that need db-interacting arguments.

        inputFileList: a list of input files to be added to commandline as the last arguments.
            they would also be added as the job's dependent input.
        extraDependentInputLs: purely for dependency purpose, not added as input arguments.
            So if files have been put in inputFileList, then they shouldn't be in extraDependentInputLs.
        """
        if objectWithDBArguments is None:
            objectWithDBArguments = self
        job = self.addGenericJob(executable=executable, \
                        inputFile=inputFile, inputArgumentOption=inputArgumentOption, \
                        outputFile=outputFile, outputArgumentOption=outputArgumentOption, \
                        inputFileList=inputFileList, argumentForEachFileInInputFileList=argumentForEachFileInInputFileList, \
                        parentJobLs=parentJobLs, \
                        extraDependentInputLs=extraDependentInputLs, extraOutputLs=extraOutputLs, \
                        transferOutput=transferOutput, extraArguments=extraArguments, extraArgumentList=extraArgumentList,\
                        job_max_memory=job_max_memory, sshDBTunnel=sshDBTunnel, key2ObjectForJob=key2ObjectForJob,\
                        objectWithDBArguments=objectWithDBArguments, walltime=walltime,\
                        **keywords)

        #set the job.input
        if getattr(job, 'input', None) is None and job.inputLs:
            job.input = job.inputLs[0]
        return job
    
    def addData2DBJob(self, executable=None, inputFile=None, inputArgumentOption="-i", \
                    inputFileList=None, argumentForEachFileInInputFileList=None,\
                    outputFile=None, outputArgumentOption="-o", \
                    data_dir=None, logFile=None, commit=False,\
                    parentJobLs=None, extraDependentInputLs=None, extraOutputLs=None, transferOutput=False, \
                    extraArguments=None, extraArgumentList=None, job_max_memory=200,  sshDBTunnel=None, \
                    key2ObjectForJob=None, objectWithDBArguments=None, **keywords):
        """
        a generic wrapper for jobs that "inserts" data (from file) into database
        Example:
            job = self.addData2DBJob(executable=executable, inputFile=None, inputArgumentOption="-i", \
                    outputFile=None, outputArgumentOption="-o", inputFileList=None, \
                    data_dir=None, logFile=logFile, commit=commit,\
                    parentJobLs=parentJobLs, extraDependentInputLs=extraDependentInputLs, \
                    extraOutputLs=None, transferOutput=transferOutput, \
                    extraArguments=extraArguments, extraArgumentList=extraArgumentList, \
                    job_max_memory=job_max_memory,  sshDBTunnel=sshDBTunnel, walltime=walltime,\
                    key2ObjectForJob=None, objectWithDBArguments=self, **keywords)

        """
        if extraArgumentList is None:
            extraArgumentList = []
        if extraOutputLs is None:
            extraOutputLs = []

        if data_dir:
            extraArgumentList.append('--data_dir %s'%(data_dir))
        if commit:
            extraArgumentList.append('--commit')
        if logFile:
            extraArgumentList.extend(["--logFilename", logFile])
            extraOutputLs.append(logFile)
        #do not pass the inputFileList to addGenericJob() because db arguments need to be added before them.
        job = self.addDBJob(executable=executable, inputFile=inputFile, \
                        inputArgumentOption=inputArgumentOption, \
                        inputFileList=inputFileList, argumentForEachFileInInputFileList=argumentForEachFileInInputFileList,\
                        outputFile=outputFile, \
                        outputArgumentOption=outputArgumentOption, \
                        parentJobLs=parentJobLs, \
                        extraDependentInputLs=extraDependentInputLs, extraOutputLs=extraOutputLs, \
                        transferOutput=transferOutput, extraArguments=extraArguments, extraArgumentList=extraArgumentList,\
                        job_max_memory=job_max_memory, sshDBTunnel=sshDBTunnel, key2ObjectForJob=key2ObjectForJob,\
                        objectWithDBArguments=objectWithDBArguments, **keywords)
        return job

    def addJobUse(self, job=None, file=None, transfer=True, register=True, link=None):
        """
        check whether a file is a use of a job already.
        """
        use = Use(file.name, link=link, register=register, transfer=transfer, optional=None, \
                                namespace=job.namespace,\
                                version=job.version, executable=None)	#, size=None
        if job.hasUse(use):
            return False
        else:
            if link==Link.INPUT:
                if hasattr(job, "inputLs"):
                    job.inputLs.append(file)
            elif link==Link.OUTPUT:
                if hasattr(job, "outputLs"):
                    job.outputLs.append(file)
            job.addUse(use)
            return True

    def addJobDependency(self, parentJob=None, childJob=None):
        """
        make sure parentJob is of instance Job, sometimes, it could be a fake job, like PassingData(output=...).
        check whether the dependency exists already.
        """
        addedOrNot = True
        if isinstance(parentJob, Job):
            dep = Dependency(parent=parentJob, child=childJob)
            if not self.hasDependency(dep):
                self.addDependency(dep)
                addedOrNot = True
            else:
                addedOrNot = False
        else:
            #sys.stderr.write("Warning: parent job %s is not a Job-instance.\n"%(repr(parentJob)))
            addedOrNot = False
        return addedOrNot

    def addDBArgumentsToOneJob(self, job=None, objectWithDBArguments=None):
        """
        use long arguments , rather than short ones.
        A convenient function to add db-related arguments to a db-interacting job.
        """
        if objectWithDBArguments is None:
            objectWithDBArguments = self
        job.addArguments("--drivername", objectWithDBArguments.drivername, "--hostname", objectWithDBArguments.hostname, \
                        "--dbname", objectWithDBArguments.dbname, \
                        "--db_user", objectWithDBArguments.db_user, "--db_passwd %s"%objectWithDBArguments.db_passwd)
        if objectWithDBArguments.schema:
            job.addArguments("--schema", objectWithDBArguments.schema)
        if getattr(objectWithDBArguments, 'port', None):
            job.addArguments("--port=%s"%(objectWithDBArguments.port))
        return job
    
    def addGenericJob(self, executable=None, inputArgumentOption="", inputFile=None, \
            outputArgumentOption="", outputFile=None, \
            inputFileList=None, argumentForEachFileInInputFileList=None, \
            frontArgumentList=None, extraArgumentList=None, extraArguments=None, \
            parentJob=None, parentJobLs=None, extraDependentInputLs=None, extraOutputLs=None, \
            transferOutput=False, sshDBTunnel=None, \
            key2ObjectForJob=None, objectWithDBArguments=None, objectWithDBGenomeArguments=None,\
            no_of_cpus=None, job_max_memory=200, walltime=180, \
            max_walltime=None, **keywords):
        """
        A generic job adding function for other functions to use.
        The commandline order:
            executable [frontArgumentList] [DBArguments] [inputArgumentOption] [inputFile] [outputArgumentOption] [outputFile]
                [extraArgumentList] [extraArguments]

        job_max_memory: integer, unit in MB.
        max_walltime: integer, in minutes. maximum possible walltime for one or a cluster of jobs.
        walltime: walltime (max running time) for a single job. 
            For a clustered job, walltime is multiplied by the cluster_size, but less than max_walltime.
        objectWithDBArguments: an object that contains database arguments (host, dbname, username, etc.).
        argumentForEachFileInInputFileList: to be added in front of each file in inputFileList.
        frontArgumentList: a list of arguments to be put in front of anything else.
        parentJob: similar to parentJobLs, but only one job.
        inputFileList: a list of input files to be added to commandline as the last arguments
            they would also be added as the job's dependent input.
            Difference from extraDependentInputLs: the latter is purely for dependency purpose, not added as input arguments.
                So if a file has been put in inputFileList, then it shouldn't be in extraDependentInputLs.
        If transferOutput is None, do not register output files as OUTPUT with transfer flag
        key2ObjectForJob: which is a dictionary with strings as key, to set key:object for each job
        job.outputLs: to hold more output files.
            If job.output is not set, set it to the 1st entry of job.outputLs
        """
        job = Job(namespace=self.namespace, name=executable.name, version=self.version)
        job.outputLs = []	# to hold more output files
        job.inputLs = []
        if frontArgumentList:
            job.addArguments(*frontArgumentList)
        if objectWithDBArguments:
            self.addDBArgumentsToOneJob(job=job, objectWithDBArguments=objectWithDBArguments)
        if objectWithDBGenomeArguments:
            self.addDBGenomeArgumentsToOneJob(job=job, objectWithDBArguments=objectWithDBGenomeArguments)

        if inputFile:
            if inputArgumentOption:
                job.addArguments(inputArgumentOption)
            job.addArguments(inputFile)
            isAdded = self.addJobUse(job, file=inputFile, transfer=True, register=True, link=Link.INPUT)
            job.input = inputFile
            #job.inputLs.append(inputFile)
        if outputFile:
            if outputArgumentOption:
                job.addArguments(outputArgumentOption)
            job.addArguments(outputFile)
            if transferOutput is not None:
                self.addJobUse(job, file=outputFile, transfer=transferOutput, register=True, link=Link.OUTPUT)
            job.output = outputFile
            #job.outputLs.append(outputFile)
        if extraArgumentList:
            job.addArguments(*extraArgumentList)

        if extraArguments:
            job.addArguments(extraArguments)

        # scale walltime according to cluster_size
        cluster_size = self.getExecutableClusterSize(executable)
        if cluster_size is not None and cluster_size and walltime is not None:
            cluster_size = int(cluster_size)
            if cluster_size>1:
                if max_walltime is None:
                    max_walltime = self.max_walltime
                walltime = min(walltime*cluster_size, max_walltime)

        setJobResourceRequirement(job, job_max_memory=job_max_memory, sshDBTunnel=sshDBTunnel,\
                            no_of_cpus=no_of_cpus, walltime=walltime)
        self.addJob(job)
        job.parentJobLs = []
        if parentJob:
            isAdded = self.addJobDependency(parentJob=parentJob, childJob=job)
            if isAdded:
                job.parentJobLs.append(parentJob)
        if parentJobLs:
            for parentJob in parentJobLs:
                if parentJob:
                    isAdded = self.addJobDependency(parentJob=parentJob, childJob=job)
                    if isAdded:
                        job.parentJobLs.append(parentJob)
        if extraDependentInputLs:
            for inputFile in extraDependentInputLs:
                if inputFile:
                    isAdded = self.addJobUse(job, file=inputFile, transfer=True, register=True, link=Link.INPUT)
                    #if isAdded:
                    #	job.inputLs.append(inputFile)
        if extraOutputLs:
            for output in extraOutputLs:
                if output:
                    job.outputLs.append(output)
                    if transferOutput is not None:
                        self.addJobUse(job, file=output, transfer=transferOutput, register=True, link=Link.OUTPUT)
        if key2ObjectForJob:
            for key, objectForJob in key2ObjectForJob.items():
                setattr(job, key, objectForJob)	#key should be a string.

        #add all input files to the last (after db arguments,) otherwise, it'll mask others (cuz these don't have options).
        if inputFileList:
            for inputFile in inputFileList:
                if inputFile:
                    if argumentForEachFileInInputFileList:
                        job.addArguments(argumentForEachFileInInputFileList)
                    job.addArguments(inputFile)
                    isAdded = self.addJobUse(job, file=inputFile, transfer=True, register=True, link=Link.INPUT)
                    #job.uses(inputFile, transfer=True, register=True, link=Link.INPUT)
                    #if isAdded:
                    #	job.inputLs.append(inputFile)
        job.outputList = job.outputLs
        #if job.output is not set, set it to the 1st entry of job.outputLs
        if getattr(job, 'output', None) is None and job.outputLs:
            job.output = job.outputLs[0]
        if getattr(job, 'input', None) is None and job.inputLs:
            job.input = job.inputLs[0]
        self.no_of_jobs += 1
        return job

    def addJavaJob(self, executable=None, jarFile=None, \
                    inputFile=None, inputArgumentOption=None, \
                    inputFileList=None,argumentForEachFileInInputFileList=None,\
                    outputFile=None, outputArgumentOption=None,\
                    frontArgumentList=None, extraArguments=None, extraArgumentList=None, extraOutputLs=None, \
                    extraDependentInputLs=None, \
                    parentJobLs=None, transferOutput=True, job_max_memory=1000,\
                    key2ObjectForJob=None, no_of_cpus=None, walltime=120, sshDBTunnel=None, **keywords):
        """
        a generic function to add Java jobs:

            fastaDictJob = self.addGenericJavaJob(executable=CreateSequenceDictionaryJava, \
                jarFile=CreateSequenceDictionaryJar, \
                inputFile=refFastaF, inputArgumentOption="REFERENCE=", \
                inputFileList=None, argumentForEachFileInInputFileList=None,\
                outputFile=refFastaDictF, outputArgumentOption="OUTPUT=",\
                parentJobLs=parentJobLs, transferOutput=transferOutput, job_max_memory=job_max_memory,\
                frontArgumentList=None, extraArguments=None, extraArgumentList=None, extraOutputLs=None, \
                extraDependentInputLs=None, no_of_cpus=None, walltime=walltime, sshDBTunnel=None, **keywords)
        """
        if executable is None:
            executable = self.java
        if frontArgumentList is None:
            frontArgumentList = []
        if extraArgumentList is None:
            extraArgumentList = []
        if extraDependentInputLs is None:
            extraDependentInputLs = []
        if extraOutputLs is None:
            extraOutputLs = []
        
        memRequirementObject = self.getJVMMemRequirment(job_max_memory=job_max_memory, minMemory=4000)
        job_max_memory = memRequirementObject.memRequirement
        javaMemRequirement = memRequirementObject.memRequirementInStr

        frontArgumentList = [javaMemRequirement, '-jar', jarFile] + frontArgumentList	#put java stuff in front of other fron arguments
        extraDependentInputLs.append(jarFile)
        job = self.addGenericJob(executable=executable, inputFile=inputFile, \
                    inputArgumentOption=inputArgumentOption,  inputFileList=inputFileList,\
                    argumentForEachFileInInputFileList=argumentForEachFileInInputFileList,\
                    outputFile=outputFile, outputArgumentOption=outputArgumentOption, \
                    parentJob=None, parentJobLs=parentJobLs, extraDependentInputLs=extraDependentInputLs, \
                    extraOutputLs=extraOutputLs, \
                    transferOutput=transferOutput, \
                    frontArgumentList=frontArgumentList, extraArguments=extraArguments, \
                    extraArgumentList=extraArgumentList, job_max_memory=job_max_memory,  sshDBTunnel=sshDBTunnel, \
                    key2ObjectForJob=key2ObjectForJob, no_of_cpus=no_of_cpus, walltime=walltime, **keywords)
        return job

    def addPipeCommandOutput2FileJob(self, executable=None, commandFile=None, \
                    outputFile=None, extraOutputLs=None, transferOutput=False, \
                    parentJobLs=None, extraDependentInputLs=None, \
                    extraArgumentList=None, sshDBTunnel=None,\
                    job_max_memory=200, walltime=120, **keywords):
        """
        Call shell/pipeCommandOutput2File to redirect stdout output to outputFile.
            shell/pipeCommandOutput2File.sh outputFile commandFile [commandArguments]
        executable can be None (Default: self.pipeCommandOutput2File).
        commandFile could be None.

        Examples:
            bwaCommand = self.registerOneExecutableAsFile(path="/usr/bin/bwa")
            extraArgumentList=[alignment_method.command]	#add mem first
            extraArgumentList.extend(["-a -M", refFastaFile] + fastqFileList)
            alignmentJob = self.addGenericPipeCommandOutput2FileJob(executable=self.BWA_Mem, commandFile=bwaCommand, \
                        outputFile=alignmentSamF, \
                        extraOutputLs=None, transferOutput=transferOutput, \
                        parentJobLs=parentJobLs, extraDependentInputLs=[refFastaFile] + fastqFileList, \
                        extraArgumentList=extraArgumentList, \
                        sshDBTunnel=None,\
                        job_max_memory=aln_job_max_memory, walltime=aln_job_walltime, no_of_cpus=no_of_aln_threads, \
                        **keywords)
            
            sortedSNPID2NewCoordinateFile = File(os.path.join(reduceOutputDirJob.output, 'SNPID2NewCoordinates.sorted.tsv'))
            sortSNPID2NewCoordinatesJob = self.addGenericPipeCommandOutput2FileJob(executable=self.pipeCommandOutput2File, \
                    commandFile=self.sortExecutableFile, \
                    outputFile=sortedSNPID2NewCoordinateFile, \
                    extraOutputLs=None, transferOutput=False, \
                    parentJobLs=[reduceJob], \
                    extraDependentInputLs=[reduceJob.output], \
                    extraArgumentList=["-k 3,3 -k4,4n -t$'\t'", reduceJob.output], \
                    sshDBTunnel=None,\
                    job_max_memory=4000, walltime=120)
            
            #skip executable
            sortedVCFFile = File(os.path.join(self.liftOverReduceDirJob.output, '%s.sorted.vcf'%(seqTitle)))
            vcfSorterJob = self.addGenericPipeCommandOutput2FileJob(commandFile=self.vcfsorterExecutableFile, \
                    outputFile=sortedVCFFile, \
                    extraOutputLs=None, transferOutput=False, \
                    parentJobLs=[selectOneChromosomeVCFJob, self.liftOverReduceDirJob], \
                    extraDependentInputLs=[self.newRegisterReferenceData.refPicardFastaDictF, selectOneChromosomeVCFJob.output], \
                    extraArgumentList=[self.newRegisterReferenceData.refPicardFastaDictF, selectOneChromosomeVCFJob.output], \
                    job_max_memory=job_max_memory, walltime=walltime)

        """
        if executable is None:
            executable = self.pipeCommandOutput2File
        if extraDependentInputLs is None:
            extraDependentInputLs = []
        if not extraArgumentList:
            extraArgumentList = []
        if commandFile:
            extraDependentInputLs.append(commandFile)
            #add commandFile in front of all other arguments
            extraArgumentList.insert(0, commandFile)
        
        job= self.addGenericJob(executable=executable, \
                    frontArgumentList=None,\
                    inputFile=None, inputArgumentOption=None,\
                    outputFile=outputFile, outputArgumentOption=None,\
                parentJobLs=parentJobLs, extraDependentInputLs=extraDependentInputLs, \
                extraOutputLs=extraOutputLs, transferOutput=transferOutput, \
                extraArgumentList=extraArgumentList, extraArguments=None, \
                key2ObjectForJob=None, job_max_memory=job_max_memory, \
                sshDBTunnel=sshDBTunnel, walltime=walltime, **keywords)
        return job
    
    def setJobOutputFileTransferFlag(self, job=None, transferOutput=False, outputLs=None):
        """
        assume all output files in job.outputLs
        """
        if outputLs is None and getattr(job, 'outputLs', None):
            outputLs = job.outputLs

        for output in outputLs:
            job.uses(output, transfer=transferOutput, register=True, link=Link.OUTPUT)

    def getJVMMemRequirment(self, job_max_memory=5000, minMemory=500, permSizeFraction=0,
                        MaxPermSizeUpperBound=35000):
        """
        Java 8 does not support PermSize anymore. set permSizeFraction to 0.
        handle when job_max_memory is None and minMemory is None.
        if a job's virtual memory (1.2X=self.jvmVirtualByPhysicalMemoryRatio, of memory request) exceeds request, it'll abort.
            so set memRequirement accordingly.
        lower permSizeFraction from 0.4 to 0.2
            minimum for MaxPermSize is now minMemory/2
        job_max_memory = MaxPermSize + mxMemory, unless either is below minMemory
            added argument permSizeFraction, MaxPermSizeUpperBound
        job_max_memory could be set by user to lower than minMemory.
            but minMemory makes sure it's never too low.
        """
        if job_max_memory is None:
            job_max_memory = 5000
        if minMemory is None:
            minMemory = 500
        #permSizeFraction is set to 0 due to newer Java no longer needs it.
        permSizeFraction = 0
        #MaxPermSize_user = int(job_max_memory*permSizeFraction)
        mxMemory_user = int(job_max_memory*(1-permSizeFraction))
        #MaxPermSize= min(MaxPermSizeUpperBound, max(minMemory/2, MaxPermSize_user))
        #PermSize=MaxPermSize*3/4
        mxMemory = max(minMemory, mxMemory_user)
        msMemory = mxMemory*3/4
        #-XX:+UseGCOverheadLimit
            #Use a policy that limits the proportion of the VM's time that is spent in GC before an OutOfMemory error is thrown. (Introduced in 6.)
        #-XX:-UseGCOverheadLimit would disable the policy.
        memRequirementInStr = "-Xms%sm -Xmx%sm"%(msMemory, mxMemory)	# -XX:PermSize=%sm -XX:MaxPermSize=%sm"%\
                    #, PermSize, MaxPermSize)
        
        memRequirement = int(mxMemory*self.jvmVirtualByPhysicalMemoryRatio)
        #if a job's virtual memory (1.2X of memory request) exceeds request, it'll abort.
        return PassingData(memRequirementInStr=memRequirementInStr, memRequirement=memRequirement)

    def scaleJobWalltimeOrMemoryBasedOnInput(self, realInputVolume=10, \
                baseInputVolume=4, baseJobPropertyValue=120, \
                minJobPropertyValue=120, maxJobPropertyValue=1440):
        """
        assume it's integer.
        walltime is in minutes.
        """
        walltime = min(max(minJobPropertyValue, float(realInputVolume)/float(baseInputVolume)*baseJobPropertyValue), \
                                    maxJobPropertyValue)	#in minutes
        return PassingData(value=int(walltime))

    def addMkDirJob(self, executable=None, outputDir=None, namespace=None, version=None,\
            parentJobLs=None, extraDependentInputLs=None):
        """
        wrapper around addMkDirJob()
            i.e.
            simulateOutputDirJob = self.addMkDirJob(outputDir=simulateOutputDir)
        """
        from pymodule.pegasus import yh_pegasus
        if namespace is None:
            namespace = self.namespace
        if version is None:
            version = self.version
        if executable is None:
            executable = self.mkdirWrap

        return addMkDirJob(workflow=self, mkdir=executable, outputDir=outputDir, \
            namespace=namespace, version=version,\
            parentJobLs=parentJobLs, extraDependentInputLs=extraDependentInputLs)

    def setup_run(self):
        """
        Wrap all standard pre-run() related functions into this function.
        """
        if self.debug:
            import pdb
            pdb.set_trace()

        if getattr(self, 'db_main', None):
            session = self.db_main.session
            session.begin(subtransactions=True)

            if not self.data_dir:
                self.data_dir = self.db_main.data_dir

            if not self.local_data_dir:
                self.local_data_dir = self.db_main.data_dir

        self.workflow = self
        self.registerJars()
        self.registerCustomJars()
        self.registerExecutables()
        self.registerCustomExecutables()

        return self

    def end_run(self):
        """
        To be called in the end.
        Write the DAG to an output file and close the database connection if there is one.
        """
        # Write the DAX to stdout
        if self.isDAGWrittenToDisk:
            sys.stderr.write("Warning: the dag has been written to a file already (writeXML() has been called). No more calling.\n")
        else:
            outf = open(self.output_path, 'w')
            self.writeXML(outf)
            self.isDAGWrittenToDisk = True

        if getattr(self, 'db_main', None):	#bugfix
            session = self.db_main.session
            if self.commit:
                session.commit()
            else:
                session.rollback()

if __name__ == '__main__':
    from argparse import ArgumentParser
    ap = ArgumentParser()
    ap.add_argument("-l", "--site_handler", type=str, required=True,
            help="The name of the computing site where the jobs run and executables are stored. "
            "Check your Pegasus configuration in submit.sh.")
    ap.add_argument("-j", "--input_site_handler", type=str,
        help="It is the name of the site that has all the input files."
        "Possible values can be 'local' or the same as site_handler. If not sure, leave it alone."
        "If not given, it is asssumed to be the same as site_handler "
        " and the input files will be symlinked into the running folder."
        "If the job submission node does not share a file system with the computing site, input_site_handler=local,"
        " and the input files will be transferred to the computing site by pegasus-transfer (need setup).")
    ap.add_argument("-C", "--cluster_size", type=int, default=1,
            help="Default: %(default)s. "
            "This number decides how many of pegasus jobs should be clustered into one job. "
            "Good if your workflow contains many quick jobs. "
            "It will reduce Pegasus monitor I/O.")
    ap.add_argument("-o", "--output_path", type=str, required=True,
            help="The path to the output file that will contain the Pegasus DAG.")
    ap.add_argument("-F", "--pegasusFolderName", type=str,
            help='The path relative to the workflow running root. '
            'This folder will contain pegasus input & output. '
            'It will be created during the pegasus staging process. '
            'It is useful to separate multiple sub-workflows. '
            'If empty or None, everything is in the pegasus root.')
    ap.add_argument("--inputSuffixList", type=str,
            help='Coma-separated list of input file suffices. Used to exclude input files.'
            'If None, no exclusion. Please include the dot to the suffix, .tsv, not tsv.'
            'Common zip suffices (.gz, .bz2, .zip, .bz) will be ignored in obtaining the suffix.')
    ap.add_argument("--tmpDir", type=str, default='/tmp/',
            help='Default: %(default)s. A local folder for some jobs (MarkDup) to store temp data.'
                '/tmp/ can be too small sometimes.')
    ap.add_argument("--max_walltime", type=int, default=4320,
            help='Default: %(default)s. Maximum wall time for any job, in minutes. 4320=3 days.'
            'Used in addGenericJob(). Most clusters have upper limit for runtime.')
    ap.add_argument("--javaPath", type=str,
            help='The path to java binary. Must be provided if you have Java jobs.')
    ap.add_argument("--jvmVirtualByPhysicalMemoryRatio", type=float, default=1.2,
            help='Default: %(default)s. '
            'If a job virtual memory (usually 1.2X of JVM resident memory) exceeds request, '
            "it will be killed on some clusters. This will make sure your job requests enough memory.")
    ap.add_argument("--debug", action='store_true',
            help='Toggle debug mode.')
    ap.add_argument("--report", action='store_true',
            help="Toggle verbose mode. Default: %(default)s.")
    ap.add_argument("--needSSHDBTunnel", action='store_true',
            help="If all DB-interacting jobs need a ssh tunnel to access a database that is inaccessible to computing nodes.")
    args = ap.parse_args()
    instance = Workflow(inputSuffixList=args.inputSuffixList,  pegasusFolderName=args.pegasusFolderName, \
        output_path=args.output_path, \
        site_handler=args.site_handler, input_site_handler=args.input_site_handler, \
        cluster_size=args.cluster_size,\
        tmpDir=args.tmpDir, max_walltime=args.max_walltime, \
        javaPath=args.javaPath, jvmVirtualByPhysicalMemoryRatio=args.jvmVirtualByPhysicalMemoryRatio,\
        debug=args.debug, needSSHDBTunnel=args.needSSHDBTunnel, report=args.report)
    instance.setup_run()
    instance.end_run()
