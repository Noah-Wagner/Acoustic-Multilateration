/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package seculock;


public class User {
    private int id;
    private boolean access;
    private String fname;
    private String lname;
    
    User() {
        
    }
    
    User (int id, String fname, String lname, boolean access) {
        this.id = id;
        this.fname = fname;
        this.lname = lname;
        this.access = access;
    }
    
    public String getFirstName() {
        return fname;
    }
    public String getLastName() {
        return lname;
    }
    public boolean getAccess() {
        return access;
    }
    
    public int getAccess1() {
        return access ? 1 : 0;
    }
    public int getId() {
        return id;
    }
    public void setAccess(boolean flag) {
        this.access = flag;
    }
    
    
    @Override
    public String toString () {
        return "Name: " + fname + lname + " ID: " + id + " Access: " + access;
    }
    
    
    
}
