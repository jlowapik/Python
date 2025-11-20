def shadow(limit=200):
    def decorator(gen_func):
        def wrapper(*args, **kwargs):
            total = 0
            gen = gen_func(*args, **kwargs)

            for event in gen:
                print(event)

                parts = event.split()
                if len(parts) != 2:
                    continue

                keyword, value_str = parts
                if keyword not in ("payment", "refund", "transfer"):
                    continue

                try:
                    value = float(value_str)
                except ValueError:
                    continue

                total += value
                if total > limit:
                    print("Тіньовий ліміт перевищено. Активую схему")

            return total
        return wrapper
    return decorator


@shadow(limit=200)
def transaction_stream():
    yield "payment 120"
    yield "junk data"
    yield "refund 50"
    yield "transfer 300"
    yield "unknown 10"
    yield "payment xyz"
    yield "payment 20"

result = transaction_stream()
print("Фінальна сума:", result)