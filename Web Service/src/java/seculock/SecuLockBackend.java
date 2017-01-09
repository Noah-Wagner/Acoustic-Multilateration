/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package seculock;

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
@Path("SecuLock")
public class SecuLockBackend {
    
    
    

    @Context
    private UriInfo context;
    
    private static final String server = "localhost";
    private static final String database = "carddb";
    private static final String username = "root";

    /**
     * Creates a new instance of SecuLockBackend
     */
    public SecuLockBackend() {
    }

    /**
     * Retrieves representation of an instance of seculock.SecuLockBackend
     * @return an instance of java.lang.String
     */
    @GET
    @Produces(MediaType.TEXT_HTML)
    public String getHtml() {
        //TODO return proper representation object
        throw new UnsupportedOperationException();
    }

    /**
     * PUT method for updating or creating an instance of SecuLockBackend
     * @param content representation for the resource
     */
    @PUT
    @Consumes(MediaType.TEXT_HTML)
    public void putHtml(String content) {
    }
    
    @GET
    @Path("updateloc")
    @Produces(MediaType.APPLICATION_JSON)
    public String activateUser (@QueryParam("x") double x, @QueryParam("y") double y) {
        System.out.println("activateUser"); 
       boolean res = false;
        try {
            res = SecuLockHandler.activate(admin_id, user_id);
        } catch (Exception ex) {
            Logger.getLogger(SecuLockBackend.class.getName()).log(Level.SEVERE, null, ex);
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
    @Path("deactivate")
    @Produces(MediaType.APPLICATION_JSON)
    public String deactivateUser (@QueryParam("admin_id") int admin_id, @QueryParam("user_id") int user_id) {
        System.out.println("deactivateUser");
        boolean res = false;
        try {
            res = SecuLockHandler.deactivate(admin_id, user_id);
        } catch (Exception ex) {
            Logger.getLogger(SecuLockBackend.class.getName()).log(Level.SEVERE, null, ex);
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
    @Path("getList")
    @Produces(MediaType.APPLICATION_JSON)
    public String getList (@QueryParam("admin_id") int admin_id, @QueryParam("access") boolean access) {
        System.out.println("getList");
        
        
        ArrayList<User> activeUsers = SecuLockHandler.getList(admin_id, access);
        JsonArrayBuilder jsonArray = Json.createArrayBuilder();
        JsonObjectBuilder builder = Json.createObjectBuilder();
        for (User c : activeUsers) {
            System.out.println("getList");
            jsonArray.add(Json.createObjectBuilder()
            .add("fname", c.getFirstName())
            .add("lname", c.getLastName())
            .add("id", c.getId()));
        }
        builder.add("users", jsonArray);
        
        JsonObject obj = builder.build();
        
       
        return obj.toString();
    }
    
    
    
}
