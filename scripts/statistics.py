from envtest.builtins import get_dataframe_summary

def main():
    sample_data = {
        "age": [25, 30, 35, 40],
        "score": [88.5, 92.0, 79.5, 95.0],
        "department": ["IT", "HR", "IT", "Finance"]
    }
    print("Testing environment with Pandas...")
    
    try:
        summary = get_dataframe_summary(sample_data)
        print("\nSuccess! Pandas is installed and working.")
        print("Calculated Averages:")
        for column, mean_val in summary.items():
            print(f" - {column}: {mean_val:.2f}")
    except ModuleNotFoundError as e:
        print(f"\nEnvironment test failed. Dependency missing: {e}")
        print("Ensure your conda environment is activated and pandas is installed.")

if __name__ == "__main__":
    main()