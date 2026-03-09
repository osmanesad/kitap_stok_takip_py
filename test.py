"""Proje bağımlılıklarını hızlıca doğrular.

Not: Bazı sistemlerde GUI kütüphanelerini doğrudan import etmek takılma yaratabildiği için
varsayılan kontrol, modülün kurulu olup olmadığını `find_spec` ile doğrular.
"""

import importlib
import importlib.util


def check_module(module_name, import_directly=False):
    try:
        if import_directly:
            importlib.import_module(module_name)
        else:
            if importlib.util.find_spec(module_name) is None:
                raise ModuleNotFoundError(module_name)
        return True, f"{module_name}: OK"
    except Exception as exc:
        return False, f"{module_name}: HATA -> {exc}"


if __name__ == "__main__":
    checks = [
        ("sqlite3", True),
        ("pandas", False),
        ("openpyxl", False),
        ("PyQt5", False),
        ("kitap_stok", False),
    ]
    has_error = False

    for module, import_directly in checks:
        ok, message = check_module(module, import_directly=import_directly)
        print(message)
        has_error = has_error or not ok

    if has_error:
        raise SystemExit(1)

    print("Tüm temel bağımlılıklar doğrulandı.")
