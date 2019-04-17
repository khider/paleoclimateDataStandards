[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![license](https://img.shields.io/github/license/khider/paleoclimateDataStandards.svg)]()
[![NSF-1541029](https://img.shields.io/badge/NSF-1541029-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1541029)

# PaleoBest: A Crowdsourced Reporting Standard for Paleoclimate Data

This repository contains code and data to reproduce the figures from the manuscript. All Figures are available in the `Figures` and `SuppFigures` directories in this repository.

Note: Data and figures will be added upon publication.

## Table of Contents
* [Data](#data)
  * [Survey Results](#survey)
  * [Completeness of MD98-2181](#core)
  * [Mind Maps](#mind)
* [Software](#code)
* [Requirements](#requirements)
* [Contact](#contact)
* [License](#license)
* [Disclaimer](#disclaimer)

## <a name='data'>Data</a>

### <a name='survey'> Survey Results </a>

The results of the survey were concatenated and anonymize. The summary is contained in the file `Paleoclimate Data Standards Concatenated Reponses.xlsx`.  

The file is organized into tabs representing the various [working groups](http://wiki.linked.earth/Category:Working_Group) on the LinkedEarth wiki and is further divided into the section focus (e.g., trace metals in foraminifera). The first column refers to whether the question applied to legacy or new dataset, the second column contains the property being voted on, the next columns contains the number of votes in each category (essential, recommended, and desired) for the various platforms on which voting was allowed (wiki, twitter, survey).

The data is used to reproduce Figures 3-15 of the PaleoBest manuscript.

### <a name='core'> Completeness of MD98-2181 </a>

The file `MD982181_CompletenessCheck.xlsx` is used to assess how complete the MD98-2181 record from [Khider et al., 2014](https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2013PA002534) is in respect to PaleoBest. Each tab corresponds to the application of the subsection of the standard. The first column lists the applicable property, the second column the recommendation from the community and the third column whether the value for the metadata is present (1: provided, 0: not provided).

This data is used to reproduce Figure 16 of the PaleoBest manuscript.

### <a name='mind'>Mind maps</a>

The Mind Maps (Figures 5, 7-15) were produced manually using [Coggle](https://coggle.it/?lang=en-US).

Figure 5: [All Working Groups]( https://coggle.it/diagram/WqMd49MJtB8DbqfH/t/community-standards-for-paleoclimate-data-and-metadata
)  
Figure 7: [Cross-Archive Working Group](https://coggle.it/diagram/W4W9podcxp86PPvf/t/cross-archive-metadata)  
Figure 8: [Documentary Archives Working Group](https://coggle.it/diagram/W4XNNeGhIngfjHzB/t/historical-documents
)  
Figure 9: [Ice cores working group](https://coggle.it/diagram/W4XbL-GhImoyjLmd/t/ice-cores
)  
Figure 10: [Lake Sediments Working Group](https://coggle.it/diagram/W4h9m-GhIjjbm3yX/t/lake-sediments
)  
Figure 11: [Marine Sediments Working Group](https://coggle.it/diagram/W4iIkodcxlDKTK6v/t/marine-sediments
)  
Figure 12: [Speleothem Working Group](https://coggle.it/diagram/W4gwj-GhIl4VmfYP/t/speleothem
)  
Figure 13: [Tree Working Group](https://coggle.it/diagram/W4huaYdcxhdzTB9z/t/trees)  
Figure 14: [Uncertainties Working Group](https://coggle.it/diagram/W4gttodcxjfvSst0/t/uncertainties
)  
Figure 15: [Chronologies Working Group](https://coggle.it/diagram/W4hzXeGhIi5Fm0q7/t/chronologies
)  

## <a name='code'>Software</a>  

`makeNewStdMainFig.py`: Reproduces Figure 3 of the PaleoBest Manuscript, example of a survey question for a new dataset.  
`makeLegacyStdMainFig.py`: Reproduces Figure 4 of the PaleoBest Manuscript, example of a survey question for a legacy dataset.  
`makeStdsFigures.py`: Reproduces all supplementary figures from the PaleoBest Manuscript.  
`MD982181_Completeness_RadarPlot.py`: Reproduces Figure 16 of the PaleoBest manuscript.  
`mosaicplots.py:` Reproduces Figure 6 of the PaleoBest manuscript.  
`MiscCalc.py`: Calculates useful statistics.

## <a name='requirements'>Requirements</a>

Software has been tested under Python v3.6 and requires the following dependencies:
* pandas  
* numpy
* matplotlib
* textwrap
* pylab
* math
* colormap
* easydev

## <a name='contact'> Contact </a>

Please report issues to <khider@usc.edu>

## <a name='license'>License</a>

The project is licensed under the GNU Public License. Please refer to the file call license.

## <a name='disclaimer'> Disclaimer </a>

This material is based upon work supported by the National Science Foundation under Grant Number ICER-1541029. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the investigators and do not necessarily reflect the views of the National Science Foundation.
