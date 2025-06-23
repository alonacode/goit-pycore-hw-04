

# Task 1
def total_salary(path: str) -> tuple[int, float]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    _, salary = line.split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка обробки рядка: {line}")
                    continue

            if count == 0:
                return 0, 0.0

            average = total / count
            return total, average

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0.0
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
        return 0, 0.0


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# Task 2
def get_cats_info(path: str) -> list[dict[str, str]]:
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                parts = line.split(",")
                if len(parts) == 3:
                    cat_id, name, age = parts
                    cats.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при обробці файлу: {e}")
    return cats

cats_info = get_cats_info("cat.txt")
print(cats_info)

