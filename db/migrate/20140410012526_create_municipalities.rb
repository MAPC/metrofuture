class CreateMunicipalities < ActiveRecord::Migration
  def change
    create_table :municipalities do |t|
      t.string        :name
      t.integer       :muni_id
      t.multi_polygon :geom, geographic: true

      t.belongs_to :community_subtype

      t.timestamps
    end
    add_index :municipalities, :community_subtype_id
  end
end
