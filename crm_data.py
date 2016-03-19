import numpy as np 

# eta, xle, yle, zle, twist, chord
raw_crm_points = np.array([
 [0., 904.294, 0.0, 174.126, 6.7166, 536.181],
 [.1, 989.505, 115.675, 175.722, 4.4402, 468.511],
 [.15, 1032.133, 173.513, 176.834, 3.6063, 434.764],
 [.2, 1076.030, 231.351, 177.912, 2.2419, 400.835], 
 [.25, 1120.128, 289.188, 177.912, 2.2419, 366.996], 
 [.3, 1164.153, 347.026, 178.886, 1.5252, 333.157], 
 [.35, 1208.203, 404.864, 180.359, .9379, 299.317], 
 [.4, 1252.246, 462.701, 182.289, .4285, 277.288], 
 [.45, 1296.289, 520.539, 184.904, -.2621, 263], 
 [.5, 1340.329, 578.377, 188.389, -.6782, 248.973], 
 [.55, 1384.375, 636.214, 192.736, -.9436, 234.816], 
 [.60, 1428.416, 694.052, 197.689, -1.2067, 220.658], 
 [.65, 1472.458, 751.890, 203.294, -1.4526, 206.501], 
 [.7, 1516.504, 809.727, 209.794, -1.6350, 192.344], 
 [.75, 1560.544, 867.565, 217.084, -1.8158, 178.186], 
 [.8, 1604.576, 925.402, 225.188, -2.0301, 164.029], 
 [.85, 1648.616, 983.240, 234.082, -2.2772, 149.872],
 [.9, 1692.659, 1041.078, 243.625, -2.5773, 135.714], 
 [.95, 1736.710, 1098.915, 253.691, -3.1248, 121.557], 
 [1., 1780.737, 1156.753, 263.827, -3.75, 107.4]
])


le = np.vstack((raw_crm_points[:,1], 
                raw_crm_points[:,2], 
                raw_crm_points[:,3]))

te = np.vstack((raw_crm_points[:,1]+raw_crm_points[:,5], 
                raw_crm_points[:,2], 
                raw_crm_points[:,3]))

mesh = np.empty((2,20,3))
mesh[0,:,:] = le.T
mesh[1,:,:] = te.T


if __name__=="__main__": 

    import plotly.offline as plt
    import plotly.graph_objs as go

    lines = []
    line_marker = dict(color='#0066FF', width=2)
    for i in xrange(20): 
        s = go.Scatter3d(x=[le[0,i],te[0,i]], y=[le[1,i],te[1,i]], z=[le[2,i],te[2,i]], mode='lines', line=line_marker)
        lines.append(s)

        if i < 19: 
            s = go.Scatter3d(x=[le[0,i],le[0,i+1]], y=[le[1,i],le[1,i+1]], z=[le[2,i],le[2,i+1]], mode='lines', line=line_marker)
            lines.append(s)
            s = go.Scatter3d(x=[te[0,i],te[0,i+1]], y=[te[1,i],te[1,i+1]], z=[te[2,i],te[2,i+1]], mode='lines', line=line_marker)
            lines.append(s)
    
    layout = go.Layout(
        title='Wireframe Plot',
        scene=dict(
            xaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            yaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            zaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            aspectmode="data"

        ),
        showlegend=False,
    )
    fig = go.Figure(data=lines, layout=layout)
    plt.plot(fig, filename="wing_top_view.html")
