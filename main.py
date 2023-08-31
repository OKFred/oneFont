from fontTools.ttLib import TTFont
import os

### 从一个TTF可变字体文件中，
### 提取所需要的字体
### 比如加粗 Bold

current_directory = os.getcwd()  # 获取当前工作目录
ttf_filename = 'SourceHanSansCN-VF.ttf'     # TTF 文件的文件名
variant_ttf_path = os.path.join(current_directory, ttf_filename)
#variant_ttf_path = '"SourceHanSansCN-VF.ttf"'  # Replace with the path to your variant TTF file
output_ttf_path = '"bold.ttf"'  # Replace with the desired output TTF file path

# Open the variant TTF file
variant_font = TTFont(variant_ttf_path)

# Specify the style (e.g., 'Regular', 'Bold', 'Italic') you want to extract
style_name = 'Bold'

# Create a new font with the desired style
output_font = TTFont()
output_font.setGlyphOrder(variant_font.getGlyphOrder())

# Copy necessary tables from the variant font to the output font
for table_tag in ('hhea', 'maxp', 'cmap', 'loca', 'glyf'):
    if (variant_font[table_tag]):
        variant_font[table_tag].compile(output_font)

# Set the style name for the extracted font
output_font['name'].setName(style_name, 1, 3, 1, 0x409)

# Save the output font
output_font.save(output_ttf_path)
