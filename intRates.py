from __future__ import annotations

def getInterestRate(cur_rate_df:pd.DataFrame, days_to_expire:int)->float:
    
    from gekko import GEKKO
    import numpy as np

    xm = cur_rate_df['days'].to_numpy()
    ym = cur_rate_df['value'].to_numpy()

    m = GEKKO(remote=True)
    m.x = m.Param(value=np.linspace(-1,10_800))
    m.y = m.Var()
    m.cspline(m.x,m.y,xm,ym)
    m.options.IMODE=2
    m.solve(disp=False)

    lower_bound = days_to_expire - 1
    upper_bound = days_to_expire
    p = GEKKO(remote=True)
    p.x = p.Var(value=1,lb=lower_bound,ub=upper_bound) # set lower bounds and upper bounds
    p.y = p.Var()
    # optimize this value change value to -p.y to find maximum, or +p.y to find minimum
    p.Obj(-p.y)
    p.cspline(p.x, p.y, xm, ym)
    p.solve(disp=False)

#     print(f'x = {p.x[0]:.1f}, y = {p.y[0]:.3f}')
    return p.y[0]