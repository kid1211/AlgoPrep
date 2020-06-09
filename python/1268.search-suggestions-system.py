#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()

        result = []
        for word in products:
            trie.insert(word)

        for i in range(len(searchWord)):
            result += [trie.findThree(searchWord[: i + 1])]

        return result


class TrieNode:
    def __init__(self, val=""):
        self.val = val
        self.isWord = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root

        for i in range(len(word)):
            letter = word[i]
            if letter not in node.children:
                node.children[letter] = TrieNode(word[:i + 1])
            node = node.children[letter]
        node.isWord = True

    def findThree(self, prefix):
        node = self.root

        for l in prefix:
            node = node.children.get(l)
            if node is None:
                return []

        # print(node.val)
        rtn = []
        self.findWord(node, 3, rtn)
        return rtn

    def findWord(self, node, k, rtn):
        if len(rtn) == k:
            return rtn

        if node.isWord:
            rtn.append(node.val)

        for l in "abcdefghijklmnopqrstuvwxyz":
            if l in node.children:
                self.findWord(node.children[l], k, rtn)

        return rtn


# @lc code=end
["ilpxatcgvfbmfunpljkodnbfaowi", "ilpsokmmniywxgbeqrpsaqeqn", "talrnwemajlqicbkxjyf", "sbqhbuvkvntmsutdpyavojqwinxofhvhecbtjjkwdkaazftxvgvicgio", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiameutvrtqwucjp", "l", "ilpxywtmdnlil", "rnjutrkyojwumoyrgzx", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiyrhxnvfqsuymujmvkwctobnuvrusbqt", "ilpxatcgvfblxfvbnoxgmmpvqqvxqyuecwpbjtlzwmmcwspztjjxevjpxdnzcectypljpkjoilnvur", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnwdkwrfizkvef", "ffngjbmfkxtstjbzalnutfiybfy", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaipwtaovnfhuzu", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuamwsmzfbbtgnfsbujeotpndobpdg", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnwdnxdqkbl", "ilpxatcfeexjqxghbengdcvsljajqaxidzitqjfjpovxmijvofntfelqidcbekzecqodiralswkjqckrpz", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrklmagbqeadtwhndgodzgfejjcs", "hp", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxovkmfvxdiuceqbvczetytkfvcfykt", "ktihatqubvuvnszewdlcyfqclgwhwsrawtcpdvxwhmvaftzkrvu", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexgkoeppszhfbajvcxuaplxeobzyqe", "ilpxatcgvfblxfvbnoxgmmpvdxthphkvtcfhpevifbuzgcmxqjvtukbgeppeaufwgjbdfppxwszavitpctqthp", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqzxnhaplrwcgwjkr", "ilpxatcgvfkvqfnblpdvtesdandbeynurlcjwwrellxigbsfjccihrvfbsbtcscblctnzededcajrywkj", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypexgkrbzdzmsbimuycjfk", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirysflyamgemsnjibnfxbke", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetvkcqmhquleujnmi", "edmasudelavobnlbrj", "zgjrwqhoqvmaaasqmggcuahifrwwrfrtpvchkuvncpvugmizhpfiokijxwlssapntpecbdgwteqvfdzwu", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedopz", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnwhchcgi", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnwdtdvk", "lnpadggtvd", "xbnfiostesudukxgghwolzawxqlovbnjweddrqcisujmuhsazvetxrsyqdaidrmfomwmanghqn", "zgmmrzerbzujlgomosxmgihordwpzvbnywczhosikslzlaqfyqnrjfbqzqwvihzojyzswbdxczknclmuyhdc", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamclkswqd", "gdqdyysurpvmakyesqoeipuvxlhnffgemhvswyvkbgatxuufhbuitjwnvvigwfweiordqdhtnzagjputzale", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnr", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaxcp", "ilpxatcgvfblxfvbnoxgmmkmnlolyewtuuosejmgconmcjep", "ilpxatcgvfblxfvbnoxgmmpvimowocjrj", "ilpxatcgvfblxfvbnoxgmmpvimowoccbsqkdevdkizvlnrl", "wyeisnjhrhossmnpnexjqbkcsorccgawfgifsmwfdqqadgqdgpfoiagyxperbshwzbnoqqyjr", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcmsdqhbizk", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnwdqlhdjfflb", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnwdnxiedjqmul", "tzkwqsmwdhczbqnimbzgguyqvtywcyzkqhnkdtknumpuikfexldysotnndztwootn", "ilpxatcsfwrpusskcsmzunvejmfymcvs", "usoaljtodfybvquycywtnvivvdvbvymivvc", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiobdewutljgvugibawjskriuxeiwishfimbsinzt", "orrcvinutuqbzlaxrfhsbpjoonsjrubyrbbdghhqnwjz", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqncvydjmnouqktixtgjtvkmwciiuso", "jponpctybxuxtnigdqortyqjiobgdaehgybozbtvxalhyubibburfsjukhalynnkvjr", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxofpsbqljapaqco", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaegtshdqrhtimpvnbymwrlmvghl", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxgcyqcrmwlrjlbnqqfuhypqgiurkyapxzrdsnbeifik", "ilpxatcgvfblxfvbnoxgmmiiubtvodpzwgdgoobsbbnlfjldpqydwejvfysrwhmhg", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnwdnxdqp", "dpwgvxdrbzlh", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpufytsqrkyhiehtjkgohchjkmxcx", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiiwstxiirty", "irjbjafrvdcpqanwt", "ilpxatcgvn", "ilpxatcgvfblxfvbnoxuherdhypducgxsuftiappkjfcqvorxizvdlgswfrqveuhlzitltnushzs", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrypwuijbjublekmxhchhnaxbhbgdaqifvdrfvheqiqcswrskd", "ilpxatcgvtqdvgovjgabbmkdicgymudbikvhihpxfmpanjyp", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamiuzrrvibhkwigjgrqfhn", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnwdnxdqkbrlym", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqismi", "jtbuygbbtdyasdtcuswpbquuhswfciyndfton", "ilpxxishsvmt", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvfgdtlfrwklzcwqmbmefnxwrtkpak", "ilpxatcgvfblxfvbnoxgmmpvimowoumiglwjrzletaydenogpldiblrwpyjeqjeow", "hlwga", "ilpxatcgvfblxfvbnjyryxxfayspcrqkvyopfzspzmmhhalwjvfhsgybgkzctlqtr", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxofewrprmowynq", "qyuthohyzttitkgfrfybiuuvzzcqbddrbby", "uinnxgnuuptrxhbhplcdklstqbamsxwaeubppeutqlgngtgzycxpcqjabucoi", "ilpxatcgvfblxfvrpbuumlvymcimuothjdhlsgenxxcllwfibvvcavuiuesgdjhsgoxjzechjhwnprmut", "btrvkwzfdovyyycfxwmxhutvldkblvrsmeyktlwnmdmdepjnkrzkmnerxesvycbrpghnf", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycltcndobbsywuhxohkzostnacjyhj", "dijc", "ilpxatcgvfblxfvbnoxgmmpvimowoccdednjkkgwtekjv", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcwqxooniui", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiyuhbnoibkpmygmul", "potullxiksrpnhngusckddvrtylgwztzxmmgvtrlbgwkgbgohsgbljroghmpwrwupszmkv", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoqpodgpsgmlj", "ryfoisftsawa", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnwdnxdqexqy", "fzvfyiqrwbserbdnnymmcaokpasfpijvbwdxnbctzekkgcudayqlnsclgcxkaeslihczwxphyqbdyxthpuprxjb", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpvoltdohcmslq", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdeyozknywbktmyzkm", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqlc", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypsan", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiarrqyflykjdwvnvicearpou", "yfilpbgdkfmphopolcvjbemkpqcqvcxdkkolpwgco", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztckwzvayxyzaqpm", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnwdnxdqkbrlywb", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaisnakhppbhnofpnuns", "khdyqeswcmriitjysdj", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpnupiwbdseowsrurzjiscnitdqncuyzxvkuiskezqy", "ilpxatcgvfovxvhriwhgpadztzfcdfgnhktkhqhjiueszhzjpmxrzfgccxovsqxo", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnvncgupn", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetabyivtjxivaraiwg", "zvtcdlbjbnlnadytwqwrnbjomdlmmujvwpmazwbjwippucsujioeevltrrdfivkamxgjtrqckuflvpnbsbrhda", "apkqpncsbbiqstfxplizqbpriqywwjiwquzpfyhwyxfcucwcs", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetjoolenqclkstqazwb", "bjvozgbmtqdxyfirqwhebtijcwrebvdkxtxoahqsjtofybvh", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukfuxkg", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycqgxdkpnisqsfzlkmnpstbd", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnwdnxdqkbrwh", "ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnwdnxdqkygsrgv"]\r
' +
'"ilpxatcgvfblxfvbnoxgmmpvimowoccdedkaqiexrcvxpuaiypkycxoeirqztcaiamkdetaiukcnwdnxdqkbrlywrywcjmtvaleckwduejlayguredkubbcqhtiafhcsmlgdmpcdouxdyxykmujehtpkjqfbrbyehjcnymgumqwbfouubonhzhvssjmpudpvjtdlurkbwyahtclafjaztcdxstgpsvhbbyndqhfkyycxnrvitcasubhnaeolgmmmedgzqtpjjhtlkwqcnjgwehbriwiklwniobbzhegbisgwccvstmdqyneolakaakrnzhmczxdoxhelbezsggbrzlzrrecyvzvrteofqopamraasigegtovcspphlpmsxsfkouohlwdvgrttzltyojunyvmlmhjjihubmkkbrvsbbdiejimobknxcwntoaqltofqopslhzobiuqhlxivctogflejhdlulda"\r
