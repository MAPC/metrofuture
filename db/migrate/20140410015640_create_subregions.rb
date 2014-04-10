class CreateSubregions < ActiveRecord::Migration
  def change
    create_table :subregions do |t|
      t.string :name
      t.string :abbr
      t.multi_polygon :geom, geographic: true

      t.timestamps
    end
  end
end
