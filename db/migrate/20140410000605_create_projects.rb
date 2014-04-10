class CreateProjects < ActiveRecord::Migration
  def change
    create_table :projects do |t|
      t.string :title
      t.text :description
      t.string :url
      t.attachment :thumbnail
      t.string :external_collaborator
      t.string :client
      t.integer :funding_source_id
      t.string :status
      t.boolean :active
      t.boolean :equity_focus
      t.text :equity_comment
      t.datetime :start_date
      t.datetime :end_date

      t.timestamps
    end
  end
end
