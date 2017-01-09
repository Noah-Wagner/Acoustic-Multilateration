/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package seculock;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

public class SecuLockHandler {
    
    public static String dbClass = "com.mysql.jdbc.Driver";
//    private static String dbName= "users";
    
    public static String dbUser = "root";
//    public static String dbPwd = "password";
    
    private static final String server = "localhost";
    private static String database = "carddb";
    public static String dbUrl = "jdbc:mysql://localhost:3306/"+ database;
    private static final String username = "root";
    
    
    @SuppressWarnings("finally")
    public static Connection createConnection() throws Exception {
        System.out.println("createConnection");
        Connection con = null;
        try {
            
            Class.forName("com.mysql.jdbc.Driver");
            
            con = DriverManager.getConnection(dbUrl, username, "");
            
            System.out.println("Connecting to database...");
        } catch (Exception e) {
            System.out.println(e);
            throw e;
        } finally {
            return con;
        }
           
    }
    
    private static ArrayList<User> getUser(int user_id) throws Exception { 
        System.out.println("getUser");
        Connection dbConn = null;
        Statement stmt = null;
        ResultSet rs = null;
        User user = null;
        ArrayList<User> users = null; 
        
        try {
            try {
                dbConn = SecuLockHandler.createConnection();
            } catch (Exception e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            
            stmt = dbConn.createStatement();
            rs = stmt.executeQuery("SELECT * FROM `cardtable` WHERE `ID` = " + user_id);
            users = new ArrayList<>();
            while (rs.next()) {
                System.out.println("THING: " + rs.getString("First Name"));
                System.out.println("THING: " + rs.getString("Last Name"));
                System.out.println("THING: " + rs.getBoolean("Access"));
                users.add(new User(rs.getInt("ID"), rs.getString("First Name"), rs.getString("Last Name"), rs.getBoolean("Access")));
                
            }
            
            
            
        } catch (SQLException sqle) {
            throw sqle;
        } catch (Exception e) {
            // TODO Auto-generated catch block
            if (dbConn != null) {
                dbConn.close();
            }
            throw e;
        } finally {
            if (dbConn != null) {
                dbConn.close();
            }
        }
        
        return users;
    }
    
    private static ArrayList<User> getUser(boolean flag) throws Exception { 
        System.out.println("getUser");
        Connection dbConn = null;
        Statement stmt = null;
        ResultSet rs = null;
        User user = null;
        ArrayList<User> users = null; 
        
        try {
            try {
                dbConn = SecuLockHandler.createConnection();
            } catch (Exception e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            
            stmt = dbConn.createStatement();
            rs = stmt.executeQuery("SELECT * FROM `cardtable` WHERE `Access` = " + flag);
            users = new ArrayList<>();
            while (rs.next()) {
                System.out.println("THING: " + rs.getString("First Name"));
                System.out.println("THING: " + rs.getString("Last Name"));
                System.out.println("THING: " + rs.getBoolean("Access"));
                users.add(new User(rs.getInt("ID"), rs.getString("First Name"), rs.getString("Last Name"), rs.getBoolean("Access")));
                
            }
            
            
            
        } catch (SQLException sqle) {
            throw sqle;
        } catch (Exception e) {
            // TODO Auto-generated catch block
            if (dbConn != null) {
                dbConn.close();
            }
            throw e;
        } finally {
            if (dbConn != null) {
                dbConn.close();
            }
        }
        
        return users;
    }
    
    private static boolean updateUser(User user) throws Exception {
        System.out.println("updateUser");
        Connection dbConn = null;
        Statement stmt = null;
        ResultSet rs = null;
        
        try {
            try {
                dbConn = SecuLockHandler.createConnection();
            } catch (Exception e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            
            stmt = dbConn.createStatement();
//            UPDATE `carddb`.`cardtable` SET `First Name` = 'Noah', `Last Name` = 'Wagner', `ID` = '2633679', `Access` = '1' WHERE `cardtable`.`ID` = 26336791;
            String update = "UPDATE `carddb`.`cardtable` SET `First Name` = '" + user.getFirstName() + "', `Last Name` = '" + user.getLastName() + "', `Access` = " + user.getAccess() + " WHERE `cardtable`.`ID` = " + user.getId();
            System.out.println(update);
            stmt.executeUpdate(update);
            
//            while (rs.next()) {
//                user = new User(rs.getInt("ID"), rs.getString("First Name"), rs.getString("Last Name"), rs.getBoolean("Access"));
//            }
            
            
        } catch (SQLException sqle) {
            throw sqle;
        } catch (Exception e) {
            // TODO Auto-generated catch block
            if (dbConn != null) {
                dbConn.close();
            }
            throw e;
        } finally {
            if (dbConn != null) {
                dbConn.close();
            }
        }
        return true;
    }
    
    
    public static boolean activate(int admin_id, int user_id) {
        ArrayList<User> users = null;
        System.out.println("activate");
        boolean success = false;
        try {
            users = getUser(user_id);
        } catch (Exception ex) {
            Logger.getLogger(SecuLockHandler.class.getName()).log(Level.SEVERE, null, ex);
        }
        if (users == null) {
            return false;
        }
        if (users.size() > 0) {
            users.get(0).setAccess(true);
            try {
                updateUser(users.get(0));
                success = true;
            } catch (Exception ex) {
                Logger.getLogger(SecuLockHandler.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
        
        return success;
    }
    
    public static boolean deactivate(int admin_id, int user_id) {
        ArrayList<User> users = null;
        System.out.println("deactivate");
        boolean success = false;
        try {
            users = getUser(user_id);
        } catch (Exception ex) {
            Logger.getLogger(SecuLockHandler.class.getName()).log(Level.SEVERE, null, ex);
        }
        if (users == null) {
            return false;
        }
        if (users.size() > 0) {
            users.get(0).setAccess(false);
            try {
                updateUser(users.get(0));
                success = true;
            } catch (Exception ex) {
                Logger.getLogger(SecuLockHandler.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
        
        return success;
    }
    
    public static ArrayList<User> getList(int admin_id, boolean active) {
        User user = null;
        System.out.println("getList " + active);
        
        ArrayList<User> users = null;
        try {
            users = getUser(active);
        } catch (Exception ex) {
            Logger.getLogger(SecuLockHandler.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        
//        System.out.println("getList: " + users.get(0).toString());
        return users;
    }
    
    
    
    
}
