# -*- coding: utf-8 -*-
'''
Create Date: 2023/09/11
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.1.4
'''

from typing import Any, Tuple

class PageContent:

    def __init__(self, *args: Any, **kwargs: Any) -> None:

        self.home_header = """\
        # Playgrounds - Classifier

        Welcome the playground that we supply the classifier model.
        """

        self.preprocessing_header = """\
        ## Data Preprocessing

        Let's begin exploring the data preprocessing of machine learning!
        """

        self.training_header = """\
        ## Training
        """

        self.dataset_choices = [
            "Titanic", 
            "Diabetes", 
            "House Prices",
        ]
