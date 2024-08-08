from facade import ScheduleFacade


class SchedulerValidator:
    def __init__(self, csv_file):
        self.schedule_facade = ScheduleFacade(csv_file)

    def run(self):
        self.schedule_facade.load_data()
        self.schedule_facade.setup_validation()
        self.schedule_facade.run_validation()
        print("Validation report validation_report.txt is generated")


if __name__ == "__main__":
    validator = SchedulerValidator("../schedules.csv")
    validator.run()
