from hw_start import insights
from baseinsight import BaseInsight


for insight in insights:
    try:
        # bi = BaseInsight(**insight)
        bi = BaseInsight.from_dict(insight)
    except Exception as error:
        print(f"{error}")
    else:
        print(bi.to_dict())

        bi['metrics'] = 'correct'  # get
        print(bi['metrics'])   # set
        del bi['metrics']   # del




