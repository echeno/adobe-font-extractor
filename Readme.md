Simple tool to extract the obfuscated fonts from Adobe CC Font Sync/Typekit.

The fonts on Windows are stored in:
	%HOME%\AppData\Roaming\Adobe\CoreSync\plugins\livetype
and on Mac:
	$HOME/Library/Application Support/Adobe/CoreSync/plugins/livetype/

Within the livetype folder are 3 folders, named "c", "e", and "r". These names are prefixed with a dot on Mac OS.

The "c" folder contains two files: entitlements.xml which is a manifest of all the fonts downloaded to your system, and entitlements-downloading.xml. I don't know for sure what entitlements-downloading.xml is for, but I presume it is only populated while a font is currently being downloaded, so I probably don't have to worry about it.

The "e" and "r" folders both contain font files, but on Windows the files in "e" are hidden. The files appear to be exactly the same in both places.

The xml structure of entitlements.xml is as follows:
	<typekitSyncState>
		<fonts type="array">
			<font>
				<url>
				<id>
				<properties>
					<fullName>
					<familyName>
					<variationName>
					<familyURL>
					<sortOrder>


Each font `id` field contains a serial number that corresponds to the obfuscated font files.

The fields we are interested in are:
	- font.id - unique ID to match to font file
	- font.properties.fullName - name to rename obfuscated file to
	- font.properties.familyName - to separate font families into their own
	folders


Both the `e` and `r` directories appear to be identical -- they are the same size, have the same number of files, and contain identical copies of the obfuscated font files.

I think fonts without extensions are OTF. Most fonts have no extension, but
some do. Fonts can have ".ttf" and ".otf" as an extension.

It is possible that the files without extensions can also be TTF.

# Font file formats
I think all the fonts are OpenType

# Program behavior
The program will be command-line only and have only these functions:
1. copy downloaded Adobe fonts to your font directory (usage: `python
		font_extract.py --install`)
2. export a folder of the deobfuscated files to a specified location (usage:
		`ccft -o %HOME%/Typekit\ Fonts`)


# general procedure
1. parse entitlements.xml
2.
