def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i, item in enumerate(lst):
        percent = (i + 1) / total
        bar_length = 60
        filled_length = int(bar_length * percent)
        bar = '=' * filled_length + '>' + '' * (bar_length - filled_length - 1)
        print(
            f"\r{int(percent * 100)}%|[{bar}]| {i + 1}/{total}",
            end='', flush=True
            )
        yield item


print()
