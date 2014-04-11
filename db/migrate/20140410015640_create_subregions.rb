class CreateSubregions < ActiveRecord::Migration
  def change
    create_table :subregions do |t|
      t.string  :name
      t.integer :muni_id
      t.string  :abbr
      t.multi_polygon :geom, geographic: true

      t.timestamps
    end
  end
end
