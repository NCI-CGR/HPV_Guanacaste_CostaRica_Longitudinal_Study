# These functions parse the file names and determine if the files are samples or blanks
# The prefix_list is in hpv_config.yaml
def is_sample(fname, prefix_list):
    if fname.split('_')[2].startswith(tuple(prefix_list)):
        return True
    else:
        return False

# Sometimes the formatting for the sample names differs from the blank names (e.g. extra underscores)
def parse_sampleID(fname):
    base = fname.split('/')[-1]
    papid = base.split('_')[2]
    olddate = base.split('_')[3]
    year = olddate[-4:len(olddate)]
    day = olddate[-6:-4]
    try:
        month = '%02d' %int(olddate[0:-6])
    except:
        month = ''
    newdate = year + month + day
    return papid + '_' + newdate


def parse_blankID(fname):
    return fname.split('_', 2)[2].rsplit('_', 3)[0]

# This is the function that Snakefile will use to parse all filenames for IDs
def parse_filenames(pname, prefix_list):
    fname= pname.split('/')[-1]
    if is_sample(fname, prefix_list):
        return parse_sampleID(fname)
    else:
        return parse_blankID(fname)

def reformat_blank_names(pname):
    blankid = parse_blankID(pname.split('/')[-1])
    rundir = pname.split('/')[-2]
    runname = [x for x in rundir.split('_') if x.startswith('S5XL')][0]
    rdid = [x for x in rundir.split('_') if x.startswith('RD')][0]
    return '_'.join([rdid, runname, blankid])





