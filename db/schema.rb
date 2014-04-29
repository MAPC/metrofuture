# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended to check this file into your version control system.

ActiveRecord::Schema.define(:version => 20140429171833) do

  create_table "community_subtypes", :force => true do |t|
    t.string   "name"
    t.string   "abbr"
    t.integer  "community_type_id"
    t.datetime "created_at",        :null => false
    t.datetime "updated_at",        :null => false
  end

  add_index "community_subtypes", ["community_type_id"], :name => "index_community_subtypes_on_community_type_id"

  create_table "community_types", :force => true do |t|
    t.string   "name"
    t.string   "abbr"
    t.datetime "created_at", :null => false
    t.datetime "updated_at", :null => false
  end

  create_table "counties", :force => true do |t|
    t.string   "name"
    t.string   "fips"
    t.datetime "created_at", :null => false
    t.datetime "updated_at", :null => false
  end

  create_table "departments", :force => true do |t|
    t.string   "name"
    t.datetime "created_at", :null => false
    t.datetime "updated_at", :null => false
  end

  create_table "funding_sources", :force => true do |t|
    t.string   "name"
    t.datetime "created_at", :null => false
    t.datetime "updated_at", :null => false
  end

  create_table "municipalities", :force => true do |t|
    t.string   "name"
    t.integer  "muni_id"
    t.spatial  "geom",                 :limit => {:srid=>4326, :type=>"multi_polygon", :geographic=>true}
    t.integer  "community_subtype_id"
    t.datetime "created_at",                                                                               :null => false
    t.datetime "updated_at",                                                                               :null => false
  end

  add_index "municipalities", ["community_subtype_id"], :name => "index_municipalities_on_community_subtype_id"

  create_table "municipalities_projects", :id => false, :force => true do |t|
    t.integer "municipality_id"
    t.integer "project_id"
  end

  add_index "municipalities_projects", ["municipality_id", "project_id"], :name => "index_municipalities_projects_on_municipality_id_and_project_id"

  create_table "municipalities_regions", :id => false, :force => true do |t|
    t.integer "municipality_id"
    t.integer "region_id"
  end

  create_table "municipalities_subregions", :id => false, :force => true do |t|
    t.integer "municipality_id"
    t.integer "subregion_id"
  end

  add_index "municipalities_subregions", ["municipality_id", "subregion_id"], :name => "index_municipalities_subregions_on_muni_id_and_subregion_id"

  create_table "projects", :force => true do |t|
    t.string   "title"
    t.text     "description"
    t.string   "url"
    t.string   "thumbnail_file_name"
    t.string   "thumbnail_content_type"
    t.integer  "thumbnail_file_size"
    t.datetime "thumbnail_updated_at"
    t.string   "external_collaborator"
    t.string   "client"
    t.integer  "funding_source_id"
    t.string   "status"
    t.boolean  "active"
    t.boolean  "equity_focus"
    t.text     "equity_comment"
    t.datetime "start_date"
    t.datetime "end_date"
    t.datetime "created_at",             :null => false
    t.datetime "updated_at",             :null => false
  end

  create_table "projects_subregions", :id => false, :force => true do |t|
    t.integer "project_id"
    t.integer "subregion_id"
  end

  add_index "projects_subregions", ["project_id", "subregion_id"], :name => "index_projects_subregions_on_project_id_and_subregion_id"

  create_table "regions", :force => true do |t|
    t.string   "name"
    t.string   "rpa_name"
    t.string   "abbr"
    t.datetime "created_at", :null => false
    t.datetime "updated_at", :null => false
  end

  create_table "strategies", :force => true do |t|
    t.integer  "number"
    t.string   "title"
    t.datetime "created_at", :null => false
    t.datetime "updated_at", :null => false
  end

  create_table "sub_strategies", :force => true do |t|
    t.string   "title"
    t.string   "letter"
    t.integer  "strategy_id"
    t.datetime "created_at",  :null => false
    t.datetime "updated_at",  :null => false
  end

  create_table "subregions", :force => true do |t|
    t.string   "name"
    t.integer  "muni_id"
    t.string   "abbr"
    t.spatial  "geom",       :limit => {:srid=>4326, :type=>"multi_polygon", :geographic=>true}
    t.datetime "created_at",                                                                     :null => false
    t.datetime "updated_at",                                                                     :null => false
  end

end
