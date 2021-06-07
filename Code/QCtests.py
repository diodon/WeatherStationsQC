## Quality Control tests


## min-max test
import numpy as np


def QCminmax(x, xmin, xmax, qc=4):
    '''
    Flag data outside minimum/maximum allowed values
    If the test fails, it return 2**order, if not 0
    :param x: numpy array time series.
    :param xmin: minimum allowed value
    :param xmax: maximum allowed values
    :param order: position in the byte string
    :return: numpy integer array of QC flags, coded as zero (no fail), 2**order (fails) or -1 as NaN
    '''
    x = np.ma.masked_invalid(x)
    x = ((x<xmin) | (x>xmax)) * qc
    x[x==0] = 1     ## recode resulting flag 0 to 1 (good data)
    return x.filled(9).astype(int)


def QCspike(x, spikeThreshold, qc=4):
    '''
    Flag data that fails spike test
    if test fails returns 2**order, if not 0
    :param x: numpy array time series
    :param spikeThreshold: threshold value for the spike test
    :param order: position in the byte string
    :return: numpy integer array of QC flags, coded as zero (no fail), 2**order (fails) or -1 as NaN
    '''
    QCx = np.abs(x[1:-1] - (x[0:-2] + x[2:])/2)
    QCx = np.ma.masked_invalid(QCx)
    QCx = np.greater(QCx, spikeThreshold) * qc
    QCx[QCx==0] = 1
    QCx = np.concatenate([np.array([0]),QCx.filled(0),np.array([0])])
    QCx[np.isnan(x)]=9
    return QCx.astype(int)



def QCflatline0(x, n, qc=4, epsilon=1e-5):
    '''
    Flag data that fails the flatline test
    :param x: numpy array time series
    :param n: length of time to evaluate the flatline
    :param epsilon: tolerance value to define a flat line
    :param order: position in the byte string
    :return: numpy integer array of QC flags, coded as zero (no fail), 2**order (fails) or -1 as NaN
    '''
    QCx = np.array([0] * len(x), dtype=int)
    x = np.ma.masked_invalid(x)
    for i in range(n-1,len(x)):
        nEqual = sum(np.abs(x[i] - x[(i-n+1):(i)]) < epsilon)
        if nEqual==n-1:
            QCx[i] = qc
        else:
                QCx[i] = 1
        QCx[np.isnan(x)] = 9
    return QCx.astype(int)


def QCflatline(x, n, qc=4, epsilon=1e-3):
    '''
    Flag data that fails the flatline test
    :param x: numpy array time series
    :param n: length of time to evaluate the flatline
    :param epsilon: tolerance value to define a flat line
    :param order: position in the byte string
    :return: numpy integer array of QC flags, coded as zero (no fail), 2**order (fails) or -1 as NaN
    '''
    QCx = pd.Series(x).rolling(n).std().to_numpy()
    QCx[QCx<epsilon] = qc
    QCx[((QCx>=epsilon) & (QCx!=qc))] = 1
    QCx[np.isnan(x)] = 9
    QCx[np.isnan(QCx)] = 0
    return QCx.astype(int)

def QCrateOfChange(x, stdMult=3, qc=4):
    '''
    Flag data that fails the flatline test
    :param x: numpy array time series
    :param stdMult: multiplier for the standard deviation of the differences as threshold
    :param order: position in the byte string
    :return: numpy integer array of QC flags, coded as zero (no qc), qc (fails) or 9 for NaNs
    '''
    QCx = np.diff(x)
    std = np.nanstd(QCx) * stdMult
    QCx[QCx>std] = qc
    QCx[((QCx<=std) & (QCx!=qc))] = 1
    QCx = np.concatenate((np.zeros(1), QCx))
    QCx[np.isnan(x)] = 9
    QCx[np.isnan(QCx)] = 0
    return QCx.astype(int)


def plotDataQC(x, qc, qcFlag=4):
    ## plot data and the flagged bad data points
    qcMask = np.ma.array(qc, mask=qc!=qcFlag)
    qcMask[qcMask==qcFlag] = 1
    xFlag = x * qcMask
    xAxis = np.arange(len(x))
    plt.plot(xAxis, x)
    plt.plot(xAxis, xFlag, '*')
    plt.show()
    return








