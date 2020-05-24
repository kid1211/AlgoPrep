public class RabinKarp {

    public int findIndexRollingHash(String source, String target) {
        int targetSize = target.length();
        if(targetSize > source.length()) return -1;
        int sourceSubStringHash = 0;
        int targetHash = 0;

        for(int i=0; i<targetSize; ++i) {
            targetHash += (target.charAt(i) - 'a') * Math.pow(26, i);
            sourceSubStringHash += (source.charAt(i) - 'a') * Math.pow(26, i);
        }

        System.out.println("outer:" + (targetHash == sourceSubStringHash));
        if(targetHash == sourceSubStringHash && source.substring(0, targetSize).equals(target)) return 0;

        int multiplier = (int) Math.pow(26,targetSize-1);
        for(int i=1; i<=source.length()-targetSize; ++i) {
            sourceSubStringHash -= (source.charAt(i - 1) - 'a');
            sourceSubStringHash /= 26;
            sourceSubStringHash += (source.charAt(i+targetSize-1) - 'a')  * multiplier;
            System.out.println(sourceSubStringHash);                                
            if (sourceSubStringHash == targetHash && source.substring(i, i+targetSize).equals(target)) return i;

        }
        return -1;
    }

    public static void main(String[] args) {
        String source = "tartarget";
        String target = "target";
        RabinKarp rk = new RabinKarp();

        System.out.println(rk.findIndexRollingHash(source, target));
    }
}

