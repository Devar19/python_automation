from pathlib import Path
from datetime import datetime

class ScreenshotUtility:

    @staticmethod
    def capture(driver, test_name):
        project_root = Path(__file__).resolve().parent.parent

        screenshot_dir = (
            project_root
            / "reports"
            / "screenshots"
        )

        screenshot_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        safe_test_name = (
            test_name
            .replace("::", "_")
            .replace("/", "_")
            .replace("\\", "_")
            .replace("[", "_")
            .replace("]", "_")
            .replace(" ", "_")
        )

        screenshot_path = (
            screenshot_dir
            / f"{safe_test_name}_{timestamp}.png"
        )

        driver.save_screenshot(
            str(screenshot_path)
        )

        return screenshot_path