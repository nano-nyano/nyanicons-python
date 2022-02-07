import colorsys

from nyanicons.hls import HLS


def format_rgb_255(color: HLS) -> str:
    rgb = colorsys.hls_to_rgb(color.h_val, color.l_val, color.s_val)
    r, g, b = (int(255*v) for v in rgb)

    return f"rgb({r}, {g}, {b})"


def format_rgb_percent(color: HLS) -> str:
    rgb = colorsys.hls_to_rgb(color.h_val, color.l_val, color.s_val)
    r, g, b = (round(100*v, 2) for v in rgb)

    return f"rgb({r}%, {g}%, {b}%)"
