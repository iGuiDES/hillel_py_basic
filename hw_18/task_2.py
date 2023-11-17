from hw_18.module.mcolor import color_text, styled, background_color, colour

poem = """
        Встала весна, чорну землю
        Сонну розбудила,
        Уквітчала її рястом,
        Барвінком укрила;
        І на полі жайворонок,
        Соловейко в гаї
        Землю, убрану весною,
        Вранці зустрічають…
        
"""


def stylization_poem(poem_text):

    style_poem = styled(poem_text)
    color_poem = color_text(style_poem, colour['black'])
    result_poem_style = background_color(color_poem)

    return result_poem_style


if __name__ == '__main__':
    result = stylization_poem(poem)
    print(result)
