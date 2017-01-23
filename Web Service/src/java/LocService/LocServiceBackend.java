/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package LocService;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.Produces;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PUT;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;

import javax.json.Json;
import javax.json.JsonArrayBuilder;
import javax.json.JsonObject;
import javax.json.JsonObjectBuilder;

/**
 * REST Web Service
 *
 * @author Noah
 */
@Path("LocService")
public class LocServiceBackend {

    @Context
    private UriInfo context;
    
    public LocServiceBackend() {
    }
    
    @GET
    @Produces(MediaType.TEXT_HTML)
    public String getHtml() {
        //TODO return proper representation object
        throw new UnsupportedOperationException();
    }

    @PUT
    @Consumes(MediaType.TEXT_HTML)
    public void putHtml(String content) {
    }
    
    @GET
    @Path("updateloc")
    @Produces(MediaType.APPLICATION_JSON)
    public String updateLocation (@QueryParam("x") double x, @QueryParam("y") double y) {
        System.out.println("updateLocation");

        boolean res = false;
        try {
            res = LocServiceHandler.updateLocation(x, y);
        } catch (Exception ex) {
            Logger.getLogger(LocServiceBackend.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        JsonObjectBuilder builder = Json.createObjectBuilder();
        if (res) {
            builder.add("response", true);
        } else {
            builder.add("response", false);
        }
        JsonObject obj = builder.build();      
        return obj.toString();
    }
   
    @GET
    @Path("getloc")
    @Produces(MediaType.APPLICATION_JSON)
    public String getLocation () {
        System.out.println("getLocation");
        Coordinates res = null;
        try {
            res = LocServiceHandler.getLocation();
        } catch (Exception ex) {
            Logger.getLogger(LocServiceBackend.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        JsonObjectBuilder builder = Json.createObjectBuilder();
        if (res != null) {
            builder.add("x", res.x);
            builder.add("y", res.y);
        } else {
            builder.add("response", false);
        }
        JsonObject obj = builder.build();      
        return obj.toString();
    }
     
}
