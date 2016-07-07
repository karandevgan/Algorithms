class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        tab_count = 0
        increase_tab_delimiter = ['{', '[']
        decrease_tab_delimeter = ['}', ']']
        return_list = []
        string_to_be_appended = ''
        for char in A:
            if char in increase_tab_delimiter:
                if string_to_be_appended.strip() != '':
                    return_list.append(string_to_be_appended)
                return_list.append('\t' * tab_count + char)
                tab_count += 1
                string_to_be_appended = '\t' * tab_count
            elif char in decrease_tab_delimeter:
                if string_to_be_appended.strip() != '':
                    return_list.append(string_to_be_appended)
                tab_count -= 1
                string_to_be_appended = '\t' * tab_count + char
                #string_to_be_appended = '\t' * tab_count
            elif char == ',':
                string_to_be_appended += char
                return_list.append(string_to_be_appended)
                string_to_be_appended = '\t' * tab_count
            else:
                string_to_be_appended += char
        return_list.append(string_to_be_appended)
        return return_list

sol = Solution()
A = '{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":null,"State":null},"vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":"SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":null,"Ads":null},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map","status":"SUCCESS","lmd":41962}]}'

for l in sol.prettyJSON(A):
    print l       