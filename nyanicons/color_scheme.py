from nyanicons.hls import HLS


class ColorScheme:
    def __init__(self, primary_color: HLS):
        self.primary: HLS = primary_color
        self.secondary: HLS
        self.tertiary: HLS
        self.secondary, self.tertiary = primary_color.triadic_complements()
        self.monochrome: HLS = primary_color.monochrome_compliment()
        self.grayscale: HLS = primary_color.desaturate()

    def __hash__(self):
        return hash((hash(self.primary),
                     hash(self.secondary),
                     hash(self.tertiary),
                     hash(self.monochrome),
                     hash(self.grayscale)))

    def __eq__(self, other):
        return hash(other) == hash(self)
