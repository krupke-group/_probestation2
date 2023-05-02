import matplotlib as mpl

def set_rcParams():
    """
    This function sets plotting parameters
    """
    mpl.rcParams['font.family'] = 'Arial'
    mpl.rcParams.update({'mathtext.default':  'regular' })
    
    mpl.rcParams['font.size'] = 12
    mpl.rcParams['axes.linewidth'] = 1
    mpl.rcParams['hatch.linewidth'] = 0.5
    mpl.rcParams['hatch.color'] = 'grey'

    mpl.rcParams['xtick.direction'] = 'out'
    mpl.rcParams['xtick.major.width'] = 1
    mpl.rcParams['xtick.minor.width'] = 1
    mpl.rcParams['xtick.major.size'] = 5
    mpl.rcParams['xtick.major.pad'] = 5
    mpl.rcParams['xtick.minor.size'] = 5
    mpl.rcParams['xtick.minor.pad'] = 5

    mpl.rcParams['ytick.direction'] = 'out'
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['ytick.minor.width'] = 1
    mpl.rcParams['ytick.major.size'] = 5
    mpl.rcParams['ytick.major.pad'] = 5
    mpl.rcParams['ytick.minor.size'] = 5
    mpl.rcParams['ytick.minor.pad'] = 5

    mpl.rcParams['figure.figsize'] = [11/2.54, 8.5/2.54]
    mpl.rcParams['figure.dpi'] = 300
    mpl.rcParams['figure.facecolor'] = 'white'