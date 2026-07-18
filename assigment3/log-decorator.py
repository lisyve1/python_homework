import logging
import functools

# one time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        positional = list(args) if args else "none"
        keyword = kwargs if kwargs else "none"

        logger.log(logging.INFO,
                    f"function: {func.__name__}\n"
                    f"positional parameters: {positional}\n"
                    f"keyword parameters: {keyword}\n"
                    f"return: {result}\n")

        return result
    return wrapper


@logger_decorator
def say_hello():
    print("Hello, World!")


@logger_decorator
def accepts_positional(*args):
    return True


@logger_decorator
def accepts_keyword(**kwargs):
    return logger_decorator


if __name__ == "__main__":
    say_hello()
    accepts_positional(1, 2, 3)
    accepts_keyword(a=1, b=2, c=3)