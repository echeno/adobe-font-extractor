import sys
import os
import argparse
import xml.etree.ElementTree as ET
from collections import namedtuple
from pprint import pprint

# global configuration object
class Config:
    path_prefix = ''
    font_dir = ''
    manifest = ''
    install_path = ''

# font data object
FontEntry = namedtuple('FontEntry', 'id name weight')

def get_font_metadata(manifest_path):
    tree = ET.parse(manifest_path)
    fonts = tree.getroot().find('fonts') # fonts list element
    
    font_data = []

    for font in fonts.findall('font'):
        props = font.find('properties')
        f = {}
        f['id'] = font.find('id').text
        f['name'] = props.find('familyName').text
        f['weight'] = props.find('variationName').text
        font_data.append(f)

    return font_data

# install the fonts per the --install flag
def install_fonts(fonts):
    pass

# extract the fonts to location
# folder structure:
# location/
#     Font1/
#         Font1 - Variation1.otf
#         Font1 - Variation2.otf
def extract_fonts(fonts, location):
    pass

def platform_setup():
    '''Set up paths'''
    c = Config()
    
    if sys.platform == 'win32':
        c.path_prefix = \
            os.path.expandvars(r'%HOME%\AppData\Roaming\Adobe\CoreSync\plugins\livetype')
        c.font_dir = os.path.join(c.path_prefix, 'r')
        c.manifest = os.path.join(c.path_prefix, r'c\entitlements.xml')
    else: # mac
        c.path_prefix = \
            os.path.expandvars(r'$HOME/Library/Application Support/Adobe/CoreSync/plugins/livetype')
        c.font_dir = os.path.join(c.path_prefix, '.r')
        c.manifest = os.path.join(c.path_prefix, '.c/entitlements.xml')

    return c

def main():
    config = platform_setup()

    
    # parse the command line arguments

    parser = argparse.ArgumentParser(description=\
        'Extract Adobe CC Typekit fonts. ' 
        'Adobe CC Font Sync syncs your fonts from Typekit, however '
        'These fonts are not available')
    #parser.add_argument('--install', type=
    parser.add_argument('-l', '--list', help='show which fonts are synced')
    parser.parse_args()



    font_data = get_font_metadata(config.manifest)
    pprint(font_data)


if __name__ == '__main__':
    main()
