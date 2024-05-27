import base64
import io
import os
from datetime import datetime, timezone

if __name__ != "__main__":
    os.environ["MPLBACKEND"] = "AGG"

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from cartopy.feature.nightshade import Nightshade


def getfig() -> plt.Figure:
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.EqualEarth())
    date = datetime.now(timezone.utc)
    ax.set_title(f"Night time shading @ {date}")
    ax.stock_img()
    ax.add_feature(Nightshade(date, alpha=0.5))

    return fig


def render() -> str:
    fig = getfig()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    plt.close(fig)

    img_str = base64.b64encode(buf.read()).decode("utf-8")
    return img_str


if __name__ == "__main__":
    import scipy

    fig = getfig()
    plt.show()
    plt.close(fig)
