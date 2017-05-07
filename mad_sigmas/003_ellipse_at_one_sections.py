import numpy as np
import pylab as pl
import mystyle as ms

pl.close('all')

Sig_11 = 10.
Sig_33 = 5.
Sig_13 = 2.

Sig_11 = 10.
Sig_33 = 5.
Sig_13 = -2.

Sig_11 = 5.
Sig_33 = 10.
Sig_13 = 2.

Sig_11 = 5.
Sig_33 = 10.
Sig_13 = -2.

R = Sig_11-Sig_33
W = Sig_11+Sig_33
T = R*R+4*Sig_13*Sig_13

sqrtT = np.sqrt(T)
signR = np.sign(R)

cos2theta = signR*R/sqrtT
costheta = np.sqrt(0.5*(1.+cos2theta))
sintheta = np.sign((Sig_11-Sig_33)*Sig_13)*np.sqrt(0.5*(1.-cos2theta))

theta = np.arctan2(sintheta, costheta)
# in sixtrack this line seems to be different different (understood, sisxtrack uses the Sigma matrix in the reference system of the strong beam)
# sintheta = -np.sign((Sig_11-Sig_33))*np.sqrt(0.5*(1.-cos2theta))

Sig_11_hat = 0.5*(W+signR*sqrtT)
Sig_33_hat = 0.5*(W-signR*sqrtT)


a = np.array([[Sig_11, Sig_13],
              [Sig_13, Sig_33]])
w, v = np.linalg.eig(a)

tt_ellip = np.linspace(0, 2*np.pi, 100)


x_ellip = []
y_ellip = []
for tt in tt_ellip:
    res = np.dot(a, np.array([np.cos(tt), np.sin(tt)]).T)
    x_ellip.append(res[0])
    y_ellip.append(res[1])
    
pl.figure(1)
pl.plot(x_ellip, y_ellip)
pl.axis('equal')
pl.grid('on')
pl.suptitle('Sig_11_hat %.2f, Sig_33_hat %.2f'%(Sig_11_hat, Sig_33_hat))

pl.plot([0, Sig_11_hat*costheta], [0, Sig_11_hat*sintheta])

pl.show()
