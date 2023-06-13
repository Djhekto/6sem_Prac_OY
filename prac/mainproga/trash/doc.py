# 1:: MPP => (BNYTR -> BNESHN) => (p<tocnoct1)
#   T => END
#   F => (1)

def euler_for_R():
    pass

def euler_for_MPP():
    pass

def mpp():
    pass

def bnytr():
    pass

def bneshn():
    pass

def main():
    # dx/dt = f(t,x) | R( x(a), x(b) )=0 | t=[a..b]
    #in: f() | p~R | t=[a..b] | t*<-[a,b]
    # //x(t*) = p
    
    # F = R( x(a,p),x(b,p) ) ~= 0 <- euler
    # dp/dt = ( [dF/dt]^-1 ) * F(p0) }
    # p(0) = p0                      } <- MPP
    
    # [dF/dt] = dR/(dx(a,p)) * dx/dp|(a,p) + dR/(dx(b,p)) * dx/dp|(b,p)  } <- BNESHN
    
    # X|(t,p) = dx/dp|(t,p) :  X/dt = f(t,p)  } 
    #                          X|t* = p       } <- BNYTR
    
    pass