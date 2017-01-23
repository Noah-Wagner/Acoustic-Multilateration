/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package LocService;

public class LocServiceHandler {
    
    private static Coordinates coords = null;
    
    public static boolean updateLocation(double x, double y) {
        coords = new Coordinates(x, y);
        return true;
    }
    
    public static Coordinates getLocation() throws Exception {
        if (coords == null) {
            throw new Exception();
        }
        return coords;
    }
    
    
    
    
}
