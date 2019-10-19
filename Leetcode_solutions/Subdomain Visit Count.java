// import java.util.*;
// class Solution {
//     public List<String> subdomainVisits(String[] cpdomains) {
//         Hashtable<String, Integer> h = new Hashtable<String, Integer>();
//         for (String domain : cpdomains){
//             String[] domainComp = domain.split(" ");
//             Integer count = Integer.parseInt(domainComp[0]);
//             String dom = domainComp[1];
//             String[] frags = dom.split(".");
//             System.out.println(frags[0]);
//             for (String frag: frags){
//                 h.put(frag, h.get(frag)+count);
//                 // h[frag] += count;
//             }
//         }
//         ArrayList<String> ans = new ArrayList<String>();
//         h.forEach((k,v)->{
//             ans.add(String.format("%s %s",v.toString(),k));
//             System.out.println(ans);
//         });
//         return ans;
//     }
// }
class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> counts = new HashMap();
        for (String domain: cpdomains) {
            String[] cpinfo = domain.split("\\s+");
            String[] frags = cpinfo[1].split("\\.");
            int count = Integer.valueOf(cpinfo[0]);
            String cur = "";
            for (int i = frags.length - 1; i >= 0; --i) {
                cur = frags[i] + (i < frags.length - 1 ? "." : "") + cur;
                counts.put(cur, counts.getOrDefault(cur, 0) + count);
            }
        }

        List<String> ans = new ArrayList();
        for (String dom: counts.keySet())
            ans.add("" + counts.get(dom) + " " + dom);
        return ans;
    }
}