import getopt
import sys

import restoration_action as ra
import procedure_ornament as po


def main(argv):
    pattern = ""

    try:
        opts, args = getopt.getopt(
            argv,
            "hu:p:",
            [
                "help",
                "pattern=",
            ],
        )
    except getopt.GetoptError:
        print("error: application.py -p <pattern>")
        print("   or: application.py --pattern=<pattern>")
        sys.exit(2)

    # 打印 返回值args列表，即其中的元素是那些不含'-'或'--'的参数。
    for i in range(0, len(args)):
        print("Parameter: %s is：%s" % (i + 1, args[i]))

    # 处理 返回值options是以元组为元素的列表。
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("command format: application.py -p <pattern>")
            print("            or: application.py --pattern=<pattern>")
            sys.exit()
        elif opt in ("-p", "--pattern"):
            pattern = arg
    print("pattern: ", pattern)

    if pattern == "0":
        po.opereation()
    elif pattern == "1":
        ra.performance()
    else:
        print("invaild option order [except 0(locking) or 1(unlocking)]")


if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名
    main(sys.argv[1:])
