import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

shoe_data = pd.read_excel("./data/shoe-data.xlsx")

print("AOV: ", shoe_data["order_amount"].mean())
print("order_amount > $20,000:\n", shoe_data.loc[shoe_data["order_amount"] > 20000])
print("user_id 607:\n", shoe_data.loc[shoe_data["user_id"] == 607])
print(
    "number of orders for 607: ",
    shoe_data.loc[shoe_data["user_id"] == 607]["order_amount"].count(),
)
print(
    "average without 607: ",
    shoe_data.loc[shoe_data["user_id"] != 607]["order_amount"].mean(),
)
print(
    "order amount using order values < $20,000: ",
    stats.tmean(shoe_data["order_amount"].to_numpy(), limits=(0, 20000)),
)

# Two sides trim_mean
print("Trimmed mean:\n5%", stats.trim_mean(shoe_data["order_amount"], 0.05))
print("10%", stats.trim_mean(shoe_data["order_amount"], 0.1))
print("15%", stats.trim_mean(shoe_data["order_amount"], 0.15))
print("20%", stats.trim_mean(shoe_data["order_amount"], 0.2))
print("25%", stats.trim_mean(shoe_data["order_amount"], 0.25))

num_bins = 50
hist_df = pd.DataFrame(
    {
        "order_amount": shoe_data["order_amount"],
        "log_order_amount": pd.DataFrame(np.log(shoe_data["order_amount"]))[
            "order_amount"
        ],
        "cuttoff_order_amount": shoe_data.loc[shoe_data["order_amount"] < 20000][
            "order_amount"
        ],
    }
)

hists = hist_df.hist(bins=num_bins)
plt.savefig("Histograms")
