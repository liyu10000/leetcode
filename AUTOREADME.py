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


def generate_text():
    text = "## LeetCode Solutions\n\n### This is the hub recording my progress on leetcode.\n\n\n"
    return text


def generate_form(N=1220, W=3):
    root = 'https://github.com/liyu10000/leetcode/blob/master'

    pyfiles = scan_files('./', postfix='.py')
    pyfiles.remove('./AUTOREADME.py')
    filemap = {}
    for f in pyfiles:
        category = os.path.basename(os.path.dirname(f))
        number = int(os.path.splitext(os.path.basename(f))[0][1:])
        filemap[number] = (category, '{}/{}/%23{}.py'.format(root, category, number))

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

    return text


def write(content):
    with open('./README.md', 'w') as f:
        f.write(content)


if __name__ == '__main__':
    content = generate_text() + generate_form()
    write(content)