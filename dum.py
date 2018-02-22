data = []
clusters = []
colors = ['rgb(228,26,28)', 'rgb(55,126,184)',]

for i in range(len(df['output'].unique())):
    name = df['output'].unique()[i]
    color = colors[i]
    x = df[df['output'] == name]['humidity']
    y = df[df['output'] == name]['temp']
    z = df[df['output'] == name]['moisture']

    trace = dict(
        name=name,
        x=x, y=y, z=z,
        type="scatter3d",
        mode='markers',
        marker=dict(size=2, color=color, line=dict(width=0)))
    data.append(trace)

    cluster = dict(
        color=color,
        opacity=0.3,
        type="mesh3d",
        x=x, y=y, z=z)
    data.append(cluster)

layout = dict(
    width=800,
    height=550,
    autosize=False,
    title='Dataset',
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
        aspectratio=dict(x=1, y=1, z=0.7),
        aspectmode='manual'
    ),
)

fig = dict(data=data, layout=layout)

# IPython notebook
py.iplot(fig, filename='pandas-3d-scatter-iris', validate=False)
