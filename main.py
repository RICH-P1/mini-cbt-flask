from models import FuelDispenser, CarWash

def main():
    assets = [
        FuelDispenser("Pump 1", 500, 1.2),
        FuelDispenser("Pump 2", 300, 1.2),
        CarWash("Wash Bay 1", 40, 5),
        CarWash("Wash Bay 2", 25, 5)
    ]

    total_revenue = 0

    for asset in assets:
        revenue = asset.calculate_revenue()
        print(f"{asset.name} revenue: ${revenue}")
        total_revenue += revenue

    print("\nTotal Station Revenue:", total_revenue)


if __name__ == "__main__":
    main()