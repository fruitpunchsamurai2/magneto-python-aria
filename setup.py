from setuptools import setup, find_packages
import pathlib

CWD = pathlib.Path(__file__).parent

README = (CWD / "README.md").read_text()

setup(
    name='MirrorX',
    version='6.0.4',
    packages=find_packages(),
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/iamliquidx/mirrorx',
    license='GPL3.0',
    author='',
    author_email='',
    include_package_data=True,
    description='Telegram Mirror Bot',
    platforms="any",
    install_requires=[
        "requests==2.26.0",
        "appdirs==1.4.4",
        "aria2p==0.10.4",
        "progress==1.6",
        "psutil==5.8.0",
        "python-telegram-bot==13.7",
        "google-api-python-client==2.11.0",
        "google-auth-httplib2==0.1.0",
        "google-auth-oauthlib==0.4.5",
        "js2py==0.71",
        "python-dotenv==0.19.0",
        "tenacity==8.0.1",
        "python-magic==0.4.24",
        "beautifulsoup4==4.9.3",
        "Pyrogram",
        "TgCrypto",
        "yt-dlp",
        "lxml==4.6.3",
        "telegraph==1.4.1",
        "speedtest-cli==2.1.3",
        "messages==0.5.0",
        "pybase64==1.1.4",
        "lk21==1.6.0",
        "megasdkrestclient"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 5 - Production/Stable"
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts":[
            "MirrorXBot = bot.__main__:main"
        ]

    },
    package_data={
        "": ["data/*.dat", "data/aria.conf"],
    },
    scripts=['bin/extract', 'bin/pextract', 'bin/MirrorX'],
)
