import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from generator import StaticSiteGenerator


class BuildTests(unittest.TestCase):
    def test_build_generates_page_with_declared_markdown_extensions(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            input_dir = root / "content"
            output_dir = root / "site"
            input_dir.mkdir()
            (input_dir / "index.md").write_text(
                "---\ntitle: Smoke Test\n---\n\n# Hello\n\nBuild output.\n",
                encoding="utf-8",
            )
            generator = StaticSiteGenerator(
                input_dir=input_dir,
                output_dir=output_dir,
                config_file=root / "config.yaml",
            )
            generator.build()

            page = output_dir / "index.html"
            self.assertTrue(page.exists())
            self.assertIn("Smoke Test", page.read_text(encoding="utf-8"))
            self.assertEqual(len(generator.pages), 1)
            self.assertIn("Build output.", generator.pages[0]["content"])

    def test_build_fails_when_markdown_processing_fails(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            input_dir = root / "content"
            input_dir.mkdir()
            source = input_dir / "broken.md"
            source.write_text("# Broken\n", encoding="utf-8")
            generator = StaticSiteGenerator(
                input_dir=input_dir,
                output_dir=root / "site",
                config_file=root / "config.yaml",
            )
            with patch.object(generator, "process_file", return_value=None):
                with self.assertRaisesRegex(RuntimeError, "Failed to process 1 Markdown file"):
                    generator.build()


if __name__ == "__main__":
    unittest.main()
