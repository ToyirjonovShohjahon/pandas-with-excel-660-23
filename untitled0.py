# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kJ6ifecqmfj2AIRoIJ6pBDJBqNLntsxq
"""

import pandas as pd
teacher=pd.DataFrame({
                'FISH':[ 'Qadamova Zulayho', "Karimov Sardor", "Azizov I", "Ibragimov N", "Xusanova M"   ],
                "Fani":[ "Suniy intelekt asoslari", "Suniy intelekt asoslari", "Bugxalteriya", "Mikroiqtisodiyot", "Kiberxafvsizlik" ],
                "Mashg'ulot turi":[ 'amaliy', "maruza", "amaliy", "maruza", "maruza" ],
                "Kafedrasi": [ "Axborot texnologiyalari", "Axborot texnologiyalari", "Kasbiy talim", "Kasbiy talim", "Axborot texnologiyalari"  ]

})
print(teacher)

teacher.to_excel("660-guruh teacher's.xlsx")