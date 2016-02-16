/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
import java.io.*;
import java.util.*;

/**
 *
 * @author suhansanu
 */
public class SingleAttackPerm {

    public static class Node {

        int id = 0;
        double src = 0;
        ArrayList<Integer> neighbor = new ArrayList<Integer>();
    }

    public static void main(String args[]) throws FileNotFoundException, IOException {

        int size = Integer.parseInt(args[0]);
        //String[] kinds = {"perm"};
        String[] kinds = {"degree", "perm", "random", "pagerank", "close"};
        for (String kind : kinds) {
            //System.out.println(kind);
            int no_of_nodes = size;
            Node[] nod = new Node[no_of_nodes];
            for (int i = 0; i < no_of_nodes; i++) {
                nod[i] = new Node();
            }
            for (int i = 0; i < no_of_nodes; i++) {
                nod[i].id = i;
                nod[i].src = 0;
            }
            String[] temp;
            //String test = "./" + no_of_nodes + "_network.txt";
            //System.out.println(test);
            try {
                FileInputStream fs = new FileInputStream(no_of_nodes + "_network.txt");
                int i = 0;
                /*
                while((i = fs.read()) != -1)
                {
                    char c=(char)i;
                    System.out.println(c);
                }*/
                DataInputStream in = new DataInputStream(fs);
                
                //System.out.println(i);
                BufferedReader br = new BufferedReader(new InputStreamReader(in));
                String strLine;
                while ((strLine = br.readLine()) != null) {
                    //System.out.println(strLine);
                    temp = strLine.split(" ");
                    /*
                    for ( String x : temp)
                    {
                        //System.out.println(x);
                    }*/
                    nod[Integer.parseInt(temp[0])].neighbor.add(Integer.parseInt(temp[1]));
                    nod[Integer.parseInt(temp[1])].neighbor.add(Integer.parseInt(temp[0]));
                }
                fs.close();

            } catch (Exception e) {
		System.out.println("here in the 1st exception ");
                System.out.println("Error is: " + e);
            }
            //System.out.println("THe Network is now ready");
	    //System.out.println(nod.length);
            int sims = 1;
            int lls = 10;
            double s_r = 0.0;
            for (int sim = 0; sim < sims; sim++) {
                double total_r = 0.0;
                for (int ll = 0; ll < lls; ll++) {
                    ArrayList<Integer> source = new ArrayList<Integer>();
                    ArrayList<Integer> intm = new ArrayList<Integer>();
                    int minimum = 0;
                    int maximum = no_of_nodes;
                    int round = 0;
                    for (int i = 0; i < no_of_nodes; i++) {
                        nod[i].src = 0;
                    }
                    //String s1 = "./" + no_of_nodes + "_seeds/" + no_of_nodes + "_size_" + kind + "_" + sim + ".txt";
                    //System.out.println("Going for" + s1);
                    FileInputStream fs = new FileInputStream("./" + no_of_nodes + "_seeds/" + no_of_nodes + "_size_" + kind + "_" + sim + ".txt");
                    DataInputStream in = new DataInputStream(fs);
                    BufferedReader br = new BufferedReader(new InputStreamReader(in));
                    String strLine;
                    while ((strLine = br.readLine()) != null) {
                        //System.out.println(strLine);
                        temp = strLine.split("\t");
                        //System.out.println(temp.length);
                        for (int i = 0; i < temp.length; i++) {
                            source.add(Integer.parseInt(temp[i]));
                            nod[Integer.parseInt(temp[i])].src = 1;
                   // System.out.println("added : " + Integer.parseInt(temp[i]));
                        }
                    }
                    fs.close();
                    /*
                    for (Integer a : source)
                    {
                        System.out.print(a+" ");
                    }*/
                    //System.out.println(source.size());
                    Random rn = new Random();
		    int count =  0;
                    while (source.size() < no_of_nodes) {
                        count = count + 1;
                        for (int i = 0; i < source.size(); i++) {
                            int m = source.get(i);
                            minimum = 0;
                            maximum = nod[m].neighbor.size() - 1;
                            int range = maximum - minimum + 1;
                            int randomNum = rn.nextInt(range) + minimum;
                            int n = nod[m].neighbor.get(randomNum);
                            if (nod[n].src == 0) {
                                nod[n].src = 1;
                                intm.add(n);
                            }
                        }
                        for (int i = 0; i < intm.size(); i++) {
                            int m = intm.get(i);
                            if (source.contains(m)) {
                                System.out.println("This should not print");
                                continue;
                            } else {
                                source.add(m);
                            }
                        }
                        intm.clear();
                        round++;
                        if (count > no_of_nodes*100)
                            break;
               // System.out.println(round + "\t" + source.size());
                    }
                    total_r += round;
                } // simulation of a particular seed for 100 times
//                    System.out.println(sim + " " + total_r / lls);
                s_r += total_r / lls;
            } // simulation of the 10 different seed 
            System.out.print( s_r / sims + "\t");
         }// kinds
    }

}
