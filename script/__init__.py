import Task1 as t1

# Main execution
if __name__ == "__main__":
    df = t1.load_data('../resources/data.csv')
    t1.calculate_statistics(df)
    t1.perform_t_test(df)
    t1.visualize(df)

    # Data Export
    df.to_csv('../resources/data_new.csv', index=False)