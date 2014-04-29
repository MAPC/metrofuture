class CreateRegions < ActiveRecord::Migration
  def change
    create_table :regions do |t|
      t.string :name
      t.string :rpa_name
      t.string :abbr

      t.timestamps
    end

    create_table :municipalities_regions, id: false do |t|
      t.integer :municipality_id
      t.integer :region_id
    end
  end

  # COPY municipalities_regions FROM '/Users/mapcuser/Projects/MetroFuture In Action/in-action/db/fixtures/relations/municipalities_regions.csv' DELIMITER ',' CSV HEADER;

end
