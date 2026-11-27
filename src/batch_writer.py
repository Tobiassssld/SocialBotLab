import pandas as pd

def save_batch(batch, output_path, first_batch):
    # Convert batch into DataFrame
    # Write CSV with appropriate mode
    # Return updated first_batch state
    batch_df = pd.DataFrame(batch)
    if first_batch:
        batch_df.to_csv(
            output_path,
            mode="w",
            index=False,
            header=True
        )
    else:
        batch_df.to_csv(
            output_path,
            mode="a",
            index=False,
            header=False
        )
    return False
