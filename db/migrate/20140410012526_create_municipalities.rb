class CreateMunicipalities < ActiveRecord::Migration
  def change
    create_table :municipalities do |t|
      t.string :name
      t.belongs_to :community_type

      t.timestamps
    end
    add_index :municipalities, :community_type_id
  end
end
