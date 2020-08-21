import os


def scan_files(directory, postfix=None):
    files_list = []
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))
    return files_list


def generate_text(n, N):
    text = f"## LeetCode Solutions ({n}/{N})\n\n### This is the hub recording my progress on leetcode.\n\n\n"
    return text


def generate_form(N, W):
    root = 'https://github.com/liyu10000/leetcode/blob/master'

    pyfiles = scan_files('./', postfix='.py') + scan_files('./', postfix='.cpp')
    pyfiles.remove('./AUTOREADME.py')
    pyfiles = [f for f in pyfiles if not 'onsite' in f]
    filemap = {}
    for f in pyfiles:
        category = os.path.basename(os.path.dirname(f))
        number, ftype = os.path.splitext(os.path.basename(f))
        number = int(number[1:])
        filemap[number] = (category, '{}/{}/%23{}{}'.format(root, category, number, ftype))

    nrows = N // W + (N % W > 0)
    text  = '|    No.    |    Category    ' * W + '|\n'
    text += '|:---------:|:--------------:' * W + '|\n'
    for i in range(nrows):
        for j in range(W):
            no = W * i + j + 1
            no = no if no <= N else ''
            if no in filemap:
                category, path = filemap[no]
                text += '|    [{}]({})    |    {}    '.format(no, path, category)
            else:
                text += '|    {}    |    {}    '.format(no, '')
        text += '|\n'

    return len(pyfiles), text


def write(content):
    with open('./README.md', 'w') as f:
        f.write(content)


if __name__ == '__main__':
    N = 1553
    W = 3  # number of columns in the form
    n, form = generate_form(N, W)
    text = generate_text(n, N)
    content = text + form
    write(content)